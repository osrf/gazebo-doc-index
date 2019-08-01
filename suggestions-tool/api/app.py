from flask import Flask, render_template, request
from rake_nltk import Rake, Metric
import requests
import numpy as np
import ast, os

rake = Rake(min_length = 1, max_length= 4, ranking_metric=Metric.WORD_DEGREE)

app = Flask(__name__,
            static_folder = "../web/dist/static",
            template_folder = "../web/dist/")

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/issues")
def issues():
    bb_completed = np.loadtxt(os.path.join(app.root_path, 'bitbucket_issues_completed.txt'), dtype=int)

    page = request.args.get('page')
    
    sort = request.args.get('sort')
    
    if sort=='votes':
        r = requests.get(url = "https://api.bitbucket.org/2.0/repositories/osrf/gazebo/issues?page=" + page + '&sort=-votes')
    else:
        r = requests.get(url = "https://api.bitbucket.org/2.0/repositories/osrf/gazebo/issues?page=" + page)

    if not r.ok:
        raise Exception("Request to Bitbucket API returned " + str(r.status_code) + " error.")
    
    data = r.json()

    for i,j in enumerate(data['values']):
    
        rake.extract_keywords_from_text(j['title'] + " " + j['content']['raw'])
        keyw_title_content = rake.get_ranked_phrases_with_scores()
        top_keyw_title_content = [a for a in keyw_title_content if a[0] >= 4]
        
        if (len(top_keyw_title_content) > 0):
            data['values'][i]['keywords'] = list(zip(*top_keyw_title_content))[1]

    if (isinstance(bb_completed.tolist(), int)):
        data['bb_completed'] = [bb_completed.tolist()]
    else:
        data['bb_completed'] = bb_completed.tolist()
        
    return data

@app.route("/issues/update", methods=["POST"])
def update():
    print("lets update")
    newly_marked = ((ast.literal_eval(request.data.decode()))['newly_marked'])
    unmarked = ((ast.literal_eval(request.data.decode()))['unmarked'])
    
    print(newly_marked)
    print(unmarked)

    bb_completed = np.loadtxt('bitbucket_issues_completed.txt', dtype=int)
    bb_completed = bb_completed.tolist()

    if (isinstance(bb_completed, int)):
        bb_completed = list(set([bb_completed]) - set(unmarked))
    else:
        bb_completed = list(set(bb_completed) - set(unmarked))
    bb_completed += newly_marked
    print(bb_completed)

    np.savetxt('bitbucket_issues_completed.txt', np.array(bb_completed), fmt='%d')
    return ''

@app.route('/favicon.ico')
def favicon():
    return 'http://gazebosim.org/assets/gazebo-0b2620068a8c04a28f40aa610daa1ce7d82cfb61be5d89eedf68fce9d11462dd.ico'
if __name__ == "__main__":
    app.run(debug=True)