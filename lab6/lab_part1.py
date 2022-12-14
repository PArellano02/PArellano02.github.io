#!/usr/bin/python3

'''
========================================
INSTRUCTIONS:
========================================

There are no pre-built functions and doctests for this lab.
This is to get you more experience writing entire python programs from scratch.

Step 1: Go to https://github.com/bpb27/trump_tweet_data_archive

Step 2: Download the files `condensed_*.json.zip`, where * is a year.
        There should be 10 total files (2009-2018).
        Trump has obviously sent tweets after 2018,
        but this particular archive of tweets has not been updated recently.

Step 3: Unzip each of these files to get files that look like `condensed_*.json`.

Step 4: Modify this `lab_part1.py` file so that it:

    1. Opens each json file and loads the file using the json library.
       Each file contains a list of tweets, and if you concatenate each file's tweets
       together you will get a list of all tweets ever sent by Donald Trump.

    2. Prints the total number of tweets.

    3. Counts the number of tweets that contain the following keywords:
       `Obama`, `Trump`, `Mexico`, `Russia`, and `Fake News`.
       It's important to remember that each of these words can appear with many different capitalizations, 
       and your program should count the word no matter how it is capitalized.  
       For example, `OBAMA`, `obama`, and `ObAmA` all need to count as an occurrence of the word `Obama`.

    4. Prints out a count of each of these words.

    My program gives the following output:

    ```
    len(tweets)= 36307
    counts= {'trump': 13924, 'russia': 412, 'obama': 2712, 'fake news': 333, 'mexico': 199}
    ```

    (Notice how I use markdown code-blocks from within python comments so you know exactly where my output starts/stops.
    It is very common to use markdown in python comments.)

    You'll know your program is correct if you get the same numbers.

Step 5: Select at least 3 more interesting words/phrases to count in trump's tweets.

Step 6: Calculate the percentage of tweets that contain each word.  (Both your new words and Trump's original tweets.)

Step 7: Display the results nicely.

    The display must have all words right justified and the percents printed with two 
    significant figures (on both sides of the decimal) as shown in the example output below.
    For example:

    ```
    percentage of tweets using phrase:
                  daca : 00.17
             fake news : 00.92
      mainstream media : 00.06
                mexico : 00.55
                 obama : 07.47
                russia : 01.13
                 trump : 38.35
                  wall : 00.91
    ```

    HINT:
    There are many ways to achieve this effect in python,
    but I recommend using the .format string function.
    Your python cheat sheet has instructions.

========================================
Submission
========================================

Upload your completed `lab_part1.py` file to sakai,
and copy and paste the output of running your program into sakai.
'''



paths = ['lab6/condensed_2009.json','lab6/condensed_2010.json', 'lab6/condensed_2011.json', 'lab6/condensed_2012.json', 'lab6/condensed_2013.json', 'lab6/condensed_2014.json','lab6/condensed_2015.json', 'lab6/condensed_2016.json','lab6/condensed_2017.json','lab6/condensed_2018.json']

import json
tweets=[]
for path in paths:
    with open(path, encoding= 'ascii') as f:
        text = f.read()
        tweets += json.loads(text)

num_tweets = 0
for tweet in tweets:
    num_tweets += 1
print('Trumpt Tweeted ', num_tweets, ' times from 2009 to 20018')



target_words = ['trump', 'obama', 'mexico', 'russia', 'fake news', 'wall' ,'policy', 'china']
for word in target_words:
    num_word = 0
    for tweet in tweets:
        if word in tweet['text'].lower():
            num_word += 1
    print('Trump mentioned ', word , num_word , ' times')


for word in target_words:
    tweet_with_word = 0
    for tweet in tweets:
        if word in tweet['text'].lower(): 
            tweet_with_word += 1 
    percentage_of_tweets = round(tweet_with_word /num_tweets *100, 2) 
    print('the word', word, 'is in', percentage_of_tweets,'% ','of the tweets')

# Step 6: Calculate the percentage of tweets that contain each word.  (Both your new words and Trump's original tweets.)

# Step 7: Display the results nicely.

#     The display must have all words right justified and the percents printed with two 
#     significant figures (on both sides of the decimal) as shown in the example output below