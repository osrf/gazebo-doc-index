from rake_nltk import Rake, Metric
import argparse
import requests 

parser = argparse.ArgumentParser()
parser.add_argument('--only_title', default=False, action='store_true', help="For extracting keywords only from title of the Bitbucket issue.")
parser.add_argument('--with_comments', default=False, action='store_true', help="For extracting keywords from the title, content (body) and comments of the Bitbucket issue.")
parser.add_argument('--min_score', default=4, help="Minimum required score of an extracted keyword.")
parser.add_argument('--min_keyw_length', default=1, help="Minimum length of an extracted keyword phrase.")
parser.add_argument('--max_keyw_length', default=4, help="Maximum length of an extracted keyword phrase.")
parser.add_argument('--sort_by_updated', default=False, action='store_true', help="To sort issues based on updation date")
parser.add_argument('--num_pages', default=1, help="Number of pages for which results will be showed. (Each page shows 25 results)")
args = parser.parse_args()

rake = Rake(min_length = args.min_keyw_length, max_length= args.max_keyw_length, ranking_metric=Metric.WORD_DEGREE)

for page in range(int(args.num_pages)):
    if not args.sort_by_updated:
        r = requests.get(url = "https://api.bitbucket.org/2.0/repositories/osrf/gazebo/issues?sort=-votes&page=" + str(page+1)) 
    else:
        r = requests.get(url = "https://api.bitbucket.org/2.0/repositories/osrf/gazebo/issues&page=" + str(page+1)) 
        
    data = r.json()
    for i,j in enumerate(data['values']):
        print ("Issue title: " + str(page * 20 + i + 1) + ': ' + j['title'])
        print ('Votes: ' + str(j['votes']))
        if args.only_title:
            rake.extract_keywords_from_text(j['title'])
            keyw_title = rake.get_ranked_phrases_with_scores()
            print(keyw_title)
        
        elif args.with_comments:
            rq = requests.get(url = j['links']['comments']['href'])
            output = rq.json()
            comments = ''
            
            rake.extract_keywords_from_text(j['title'] + " " + j['content']['raw'])
            keyw_title_content = rake.get_ranked_phrases_with_scores()
            top_keyw_title_content = [a for a in keyw_title_content if a[0] >= args.min_score]

            print("Keywords from title and content: ")
            print(top_keyw_title_content)
            
            for k in output['values']:
                comments += str(k['content']['raw'])
            
            rake.extract_keywords_from_text(comments)
            keyw_comments = rake.get_ranked_phrases_with_scores()
            top_keyw_comments = [a for a in keyw_comments if a[0]>= args.min_score]
            
            print("Keywords from comments")
            print(top_keyw_comments)
        else:
            rake.extract_keywords_from_text(j['title'] + " " + j['content']['raw'])
            keyw_title_content = rake.get_ranked_phrases_with_scores()
            top_keyw_title_content = [a for a in keyw_title_content if a[0] >= args.min_score]

            print("Keywords from title and content: ")
            if (len(top_keyw_title_content) > 0):
                print(list(zip(*top_keyw_title_content))[1])

        print('------------------------------------------------------------')
