import tweepy
import credentials
import msg
import time

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