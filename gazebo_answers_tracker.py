import requests
from bs4 import BeautifulSoup
from rake_nltk import Rake, Metric
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--min_keyw_length', default=1, help="Minimum length of an extracted keyword phrase.")
parser.add_argument('--max_keyw_length', default=4, help="Maximum length of an extracted keyword phrase.")
parser.add_argument('--min_score', default=4, help="Minimum required score of an extracted keyword.")
parser.add_argument('--print_content', default=False, action='store_true', help="To print content of question and answers")
parser.add_argument('--num_pages', default=1, help="Number of pages for which results will be showed. (Each page shows 30 results)")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

args = parser.parse_args()
rake = Rake(min_length = args.min_keyw_length, max_length= args.max_keyw_length, ranking_metric=Metric.WORD_DEGREE)

for page in range(int(args.num_pages)):
    req = requests.get('http://answers.gazebosim.org/questions/scope:all/sort:votes-desc/page:'+ str(page+1) + '/')

    if not req.ok:
        raise Exception(bcolors.FAIL + "Request returned " + str(req.status_code) + " error." + bcolors.ENDC)

    soup = BeautifulSoup(req.text, 'html.parser')
    question_list = soup.find(id='question-list')

    print('Page ' + str(page+1))
    for indx, question in enumerate(question_list(recursive=False)):

        id = question.get('id')[9:]
        question_title = (question.find('h2').find('a').text)
        rake.extract_keywords_from_text(question_title)
        
        keyw_q_title = rake.get_ranked_phrases_with_scores()
        top_keyw_q_title = [a for a in keyw_q_title if a[0] >= args.min_score]
        
        print("\n" + bcolors.BOLD + 'Question #' + str(page * 30 + indx + 1) + bcolors.ENDC)
        if (args.print_content):
            print("Question title: " + bcolors.HEADER + question_title + bcolors.ENDC)
        
        print('Keywords of question title are: ', end=" ")
        
        print(bcolors.BOLD, end="") # bold for easy visibility
        if (len(top_keyw_q_title) > 0):
            print(list(zip(*top_keyw_q_title))[1])
        print(bcolors.ENDC)

        # scraping RSS feed of question

        rss = requests.get('http://answers.gazebosim.org/feeds/question/' + id)
        soup_rss = BeautifulSoup(rss.text, "xml")

        items = soup_rss.findAll("item")

        ind = 0
        for item in items:
            if (item.title.text[:7] != 'Comment'):
                ind += 1
                if (args.print_content):
                    print('Answer is: ')
                    print(bcolors.HEADER + item.description.text + bcolors.ENDC)
                rake.extract_keywords_from_text(item.description.text)
                keyw_q_answer = rake.get_ranked_phrases_with_scores()
                top_keyw_q_answer = [a for a in keyw_q_answer if a[0] >= args.min_score]

                print('Keywords of answer ' + str(ind) + ' are: ')
                if (len(top_keyw_q_answer) > 0):
                    print(bcolors.BOLD)
                    print(list(zip(*top_keyw_q_answer))[1])
                    print(bcolors.ENDC)

        print('----------------------------------------------------------------------------')
