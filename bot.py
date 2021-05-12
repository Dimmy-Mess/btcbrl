import tweepy
#import credentials #>> For testing!
import msg
import time

from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_KEY_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)

tweeting_time = 60 
#hours = 12
#tweeting_time = 3600*hours


while True:
    api.update_status(msg.composer())
    time.sleep(tweeting_time)