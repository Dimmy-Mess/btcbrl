import tweepy
#import credentials >> For testing!
import msg
import time

from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_KEY_SECRET']

auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token,credentials.access_token_secret)
api = tweepy.API(auth)

hours = 12
tweeting_time = 3600*hours


def Tweeting():

    while True:
        
        api.update_status(msg.composer())
        time.sleep(tweeting_time)



Tweeting()