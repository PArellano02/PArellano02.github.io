tweets_str = ''' [
    {   "source": "Twitter Web Client", 
        "id_str": "6312794445", 
        "text": "Trump International Tower in Chicago ranked 6th tallest building in world by Council on Tall Buildings & Urban Habitat http://bit.ly/sqvQq", 
        "created_at": "Thu Dec 03 19:39:09 +0000 2009", 
        "retweet_count": 33,
        "favorite_count": 6
    },
    {   "source": "Twitter Web Client", 
        "id_str": "6971079756",
        "text": "From DONALD Trump: Wishing everyone a wonderful holiday & a happy, healthy, prosperous New Year. Let's think like champions in 2010!", 
        "created_at": "Wed Dec 23 17:38:18 +0000 2009",
        "retweet_count": 28,
        "favorite_count": 12
        
    }
]
'''
import json
tweets = json.loads(tweets_str)

# 'lab6' refers to folder 'condensed_2009.json'  refers to the name of the file 
# with open('lab6/condensed_2009.json', encoding = 'ascii') as f:
#     text = f.read()
#     data = json.loads(text)
#     tweets = json.loads(text)

paths = ['lab6/condensed_2009.json', 'lab6/condensed_2010.json', 'lab6/condensed_2011.json', 'lab6/condensed_2012.json', 'lab6/condensed_2013.json', 'lab6/condensed_2014.json' ]

num_trump = 0
for tweet in tweets:
    # if 'Trump' in tweet['text'] or 'trump' in tweet['text']: The other is more all encompassing 
    if 'trump' in tweet['text'].lower():
        num_trump += 1

print('num trump=', num_trump)
