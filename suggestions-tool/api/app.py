from flask import Flask, render_template, request
from rake_nltk import Rake, Metric
import requests
import numpy as np
import ast, os, nltk, re, db

nltk.download('stopwords')
nltk.download('punkt')
# stop words: set of words to be excluded from consideration while generating keywords
stopwords = nltk.corpus.stopwords.words('english')
newStopWords = ['http','https','://','```','~~~','///']
stopwords.extend(newStopWords)

rake = Rake(min_length = 1, max_length= 4, ranking_metric=Metric.WORD_DEGREE, stopwords=stopwords)
cursor = db.connect()
app = Flask(__name__,
            static_folder = "../web/dist/static",
            template_folder = "../web/dist/")

search_dir = os.path.join(app.root_path, '../../_categories/')
files =  os.listdir(search_dir)
files = [os.path.join(search_dir, f) for f in files] # add path to each file

category_list = []
for file in files:
    slash_pos = file.rfind('/')
    category_string = file[slash_pos+1:-3]
    if category_string != 'all_links':
        category_list.append(category_string)

def clean_characters(keywords_list):
    # bad_chars = ['<','>','[',']','#','!','(',')','`','"','_','*','@','%','^']
    keywords_list = list(keywords_list)
    for index,keyword in enumerate(keywords_list):
        keywords_list[index] = re.sub('[^A-Za-z0-9 ]+', '', keyword)
    return keywords_list

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/issues")
def issues():
    cursor.execute('select * from issues')
    bb_completed = cursor.fetchall()

    page = request.args.get('page')
    
    sort = request.args.get('sort')
    
    if sort=='votes':
        r = requests.get(url = "https://api.bitbucket.org/2.0/repositories/osrf/gazebo/issues?page=" + page + '&sort=-votes')
    else:
        r = requests.get(url = "https://api.bitbucket.org/2.0/repositories/osrf/gazebo/issues?page=" + page)

    if not r.ok:
        raise Exception("Request to Bitbucket API returned " + str(r.status_code) + " error.")
    
    data = r.json()

    hexaPattern = re.compile(r'0x0*[1-9a-fA-F][0-9a-fA-F]*') # regep for hex code
    numberRegExp = '\d{1,10}' # regexp for 2-10 digit numbers

    for i,j in enumerate(data['values']):
    
        rake.extract_keywords_from_text(j['title'] + " " + j['content']['raw'])
        keyw_title_content = rake.get_ranked_phrases_with_scores()
        top_keyw_title_content = [a for a in keyw_title_content if (a[0] >= 4 and not re.search(hexaPattern, a[1]) and not re.search(numberRegExp, a[1]))]
        
        if (len(top_keyw_title_content) > 0):
            data['values'][i]['keywords'] = clean_characters(list(zip(*top_keyw_title_content))[1])

    data['bb_completed'] = bb_completed
    data['category_list'] = category_list
        
    return data

@app.route("/issues/update", methods=["POST"])
def update():
    try:
        changed_categories = ((ast.literal_eval(request.data.decode()))['changed_categories'])
        for category in changed_categories: 
            if ('new_category' in category):
                cursor.execute('UPDATE issues SET index_category= \'' + category['new_category'] + '\' WHERE issue_id=' + str(category['id']))
            else:
                cursor.execute('DELETE FROM issues WHERE issue_id=' + str(category['id']))
    except Exception:
        print('Exception at updating')
    
    newly_marked = ((ast.literal_eval(request.data.decode()))['newly_marked'])
    if (len(newly_marked) > 0):
        args_str = b','.join(cursor.mogrify("(%s,%s)", list(category.values())[::-1] if type(list(category.values())[0]) is str else list(category.values()))  for category in newly_marked)
        cursor.execute("INSERT INTO issues VALUES " + args_str.decode()) 

    return ''

@app.route('/favicon.ico')
def favicon():
    return 'http://gazebosim.org/assets/gazebo-0b2620068a8c04a28f40aa610daa1ce7d82cfb61be5d89eedf68fce9d11462dd.ico'
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)