import tweepy
import json


def post_to_twitter():
    with open('config.json') as config:
        creds = json.load(config)

    try:
        auth = tweepy.OAuthHandler(creds["twitter_consumer_key"], creds["twitter_consumer_secret_key"])
        auth.set_access_token(creds["twitter_access_token"], creds["twitter_access_secret"])
        api = tweepy.API(auth)
        tweet_text = f"This is just a test of the API"
        api.update_status(tweet_text)
    except tweepy.error.TweepError as e:
        print(f'Your tweepy error is listed below!\n{e}')
post_to_twitter()


