# Web Scraper Art Project

## Description
This project is a simple web scraper that fetches data from 4chan in order to create a "positive poem" out of text from the site's /pol/ board.
Created for the course Digital Studio Art at Colgate University.

## Process
After first retrieving the data from the API with python requests, I used [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/) 
to clean the data. I then used the VADER sentiment analysis tool from [NLTK](https://www.nltk.org) in order to grab 30 sentences with positive
sentiment from the text and randomly shuffle those lines into a final "poem", an example of which is visible in poem.py. 
