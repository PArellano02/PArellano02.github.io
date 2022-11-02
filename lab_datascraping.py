'''
INSTRUCTIONS: Implement each function below so that the doctests all pass.
'''

import requests
from itertools import count
from pydoc import text
from re import X


def how_many_claremonts_in_str(s):
    '''
    returns the number of times the string 'Claremont' appears in s

    HINT:
    there is a built in string function that already implements this method;
    you can find this method listed in the Python Cheatsheet under the section
    "Generic Operations on Containers"
    >>> how_many_claremonts_in_str('This sentence is about Montclair.')
    0
    >>> how_many_claremonts_in_str('This sentence is about Claremont.')
    1
    >>> how_many_claremonts_in_str('Claremont. Claremont. Claremont. Claremont!')
    4
    '''
    # split = s.split()
    # num = 0
    # for word in split:
    #     if 'Claremont' in word:
    #         num += 1
    # return num 
    count = s.lower().count('claremont')
    return count

def how_many_claremonts_in_url(url):
    '''
    returns the number of times the string 'Claremont' appears in the webpage specified by url

    HINT:
    Use the requests library to download the text of the input url.
    The call your `how_many_claremonts_in_str` function on this text.

    WARNING:
    these values can change over time as the webpages get updated;
    the current values listed are correct for Friday, 28 October.

    >>> how_many_claremonts_in_url('https://www.cmc.edu')
    31
    >>> how_many_claremonts_in_url('https://www.hmc.edu')
    7
    >>> how_many_claremonts_in_url('https://www.pitzer.edu')
    0
    >>> how_many_claremonts_in_url('https://www.pomona.edu')
    18
    >>> how_many_claremonts_in_url('https://www.scrippscollege.edu')
    0
    '''
    r = requests.get(url)
    # text = r.text
    return how_many_claremonts_in_str(r.text)

