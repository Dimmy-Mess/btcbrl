import tweepy
import credentials
import msg
import time

auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token,credentials.access_token_secret)
api = tweepy.API(auth)


def Tweeting():

    while True:
        
        api.update_status(msg.composer())
        time.sleep(3600)



Tweeting()