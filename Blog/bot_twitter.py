import tweepy
from decouple import config


client = tweepy.Client(
    config('bearer_token'),
    config('API_Key'),
    config('API_Key_Secret'),
    config('Access_Token'),
    config('Access_Token_Secret')
)

auth = tweepy.OAuth1UserHandler(
    config('API_Key'),
    config('API_Key_Secret'),
    config('Access_Token'),
    config('Access_Token_Secret')
                                )

api=tweepy.API(auth)

client.create_tweet(text='Texta')