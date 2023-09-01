import tweepy
from decouple import config

API_KEY = config('API_Key')
API_SECRET_KEY = config('API_Key_Secret')
BEARER_TOKEN = config('bearer_token')

auth = tweepy.AppAuthHandler(API_KEY, API_SECRET_KEY)
api = tweepy.API(auth, wait_on_rate_limit=True)


query = 'livros'
tweets = api

for tweet in tweets:
    print("Username:", tweet.user.screen_name)
    print("Tweet:", tweet.full_text)