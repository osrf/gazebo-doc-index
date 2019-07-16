import requests
from bs4 import BeautifulSoup
from rake_nltk import Rake, Metric
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--min_keyw_length', default=1, help="Minimum length of an extracted keyword phrase.")
parser.add_argument('--max_keyw_length', default=4, help="Maximum length of an extracted keyword phrase.")
args = parser.parse_args()

page = requests.get('http://answers.gazebosim.org/questions/scope:all/sort:votes-desc/page:1/')
soup = BeautifulSoup(page.text, 'html.parser')
question_list = soup.find(id='question-list')

rake = Rake(min_length = args.min_keyw_length, max_length= args.max_keyw_length, ranking_metric=Metric.WORD_DEGREE)
for question in question_list(recursive=False):

    id = question.get('id')[9:]
    question_title = (question.find('h2').find('a').text)
    rake.extract_keywords_from_text(question_title)
    keyw_q_title = rake.get_ranked_phrases_with_scores()

    print(question_title)
    print(keyw_q_title)
    # scraping RSS feed of question

    rss = requests.get('http://answers.gazebosim.org/feeds/question/' + id)
    soup_rss = BeautifulSoup(rss.text, "xml")

    items = soup_rss.findAll("item")

    for item in items:
        if (item.title.text[:7] != 'Comment'):
            print('Answer is: ')
            print(item.description.text)
            rake.extract_keywords_from_text(item.description.text)
            # keyw_q_answer = rake.get_ranked_phrases_with_scores()
            keyw_q_answer = rake.get_ranked_phrases()
            print('Keywords of answer are: ')
            print(keyw_q_answer)
    
    break