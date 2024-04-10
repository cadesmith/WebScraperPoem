import requests
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import re
import random 

# helper function to clean text 
def clean_soup(text):
    soup = BeautifulSoup(text, 'html.parser')
    clean_text = soup.get_text()
    return clean_text

# helper function to convert a thread into a series of lines
def make_lines(text, poem):
    sid = SentimentIntensityAnalyzer()
    text = nltk.tokenize.sent_tokenize(text)   
    for sent in text: 
        if sid.polarity_scores(sent)['compound'] > 0.25:
            sent = clean_sentence(sent)
            split = sent.split()
            if len(split) > 15: 
                idx = random.randint(0, len(split) - 15)
                sent = ' '.join(split[idx:idx + 15])
            poem.append(sent)
            return
        
# helper function to remove post numbers using regex 
def clean_sentence(text):
    pattern = r">>\d{8}"
    return re.sub(pattern, '', text)

def main():

    r = requests.get("https://a.4cdn.org/pol/threads.json")

    # retrieves thread numbers from the first page of a board 
    threads = []
    for thread in r.json()[0]['threads']:
        threads.append(thread['no'])
    threads.pop(0) # remove board description post

    poem = []

    # retrieves text from all threads 
    for thread in threads: 
        t = requests.get("https://a.4cdn.org/pol/thread/%s.json" % thread)
        for post in t.json()['posts']: 
            if 'com' in post.keys():
                make_lines(clean_soup(post['com']), poem)

    random.shuffle(poem)
    poem = poem[:30]
    with open('poem.txt', 'w') as file:
        file.write("4chan: A Poem of Postivity")
        for line in poem: 
            file.write('\n\n' + line)
    file.close()

if __name__ == "__main__":
    main()