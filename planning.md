# A5 Planning Document

Ideas: 

**4chan scrape**
- 4chan API: https://github.com/4chan/4chan-API
- Gather posts from a board
    - Which board?
- Take all comments/posts from a page on the board
- Select a number of words from each post and comment
    - What number? Which words? Randomly?
- Rearrange these new lines into a poem 

**Process**

Only make 1 request per second! 

Scrape first (maybe more) board page in order to harvest thread numbers
    - Example link to scrape from: https://a.4cdn.org/lit/threads.json

Where /lit/ is the board 

Scrape threads for word and reply content 
    - Example link to scrape from: https://a.4cdn.org/lit/thread/23214633.json

Where /lit/ is the board and the number is the thread number. 

Sentiment analysis to determine naughty words?
    - Replace naughty words with nice ones 
    - Construct poem :smile:
        - choose random string (eight words long?) from each part of a post


twelve? or 15? word strings 
- if string is longer than 15
