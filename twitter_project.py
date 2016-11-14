import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'VM4CNuiBL9d7r8uAfLGqOK8Ys'
consumer_secret = 'HMAffXTpQmw9M1xDtT7bVke4l9BbLsyQpY9CjISn9LVGYUFQcV'
access_token = '725352201569325057-4LY2Tu1qJIJxuvcnwtSAm60wuoHvYO0'
access_secret = 'G6aQEVIWJUUpAtmfy4QErf7ZMvoKJI8ciOilLBKjF9DKH'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)


from tweepy import Stream
from tweepy.streaming import StreamListener


 

import nltk
import json
from nltk.tokenize import word_tokenize
import re
 
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens
 
thefile = open('test.txt', 'w')
with open('python.json', 'r') as f:
    for line in f:
        tweet = json.loads(line)
        tokens = preprocess(tweet['text'])
        print tokens
        for item in tokens:
          thefile.writelines(str(tokens))


