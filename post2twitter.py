import os
import json
import tweepy


def post_to_twitter():
    if os.path.exists(".\link.txt"):
        os.remove("link.txt")

    with open('./config/config.json') as config:
        data = json.load(config)

    try:
        linkText = open("link.txt", "r+")
        link = linkText.read()
    except FileNotFoundError as err:
        print(f'[+] {err}')
    
    try:
        auth = tweepy.OAuthHandler(data["twitter_consumer_key"], data["twitter_consumer_secret_key"])
        auth.set_access_token(data["twitter_access_token"], data["twitter_access_secret"])
        api = tweepy.API(auth)
        tweet_text = f"Hey everyone I have something new for you. Why don't you head over to my GitHub and check it out.\n{link}\nThis tweet brought to you by push2hub\n#python #codingisfun #automation"
        api.update_status(tweet_text)
        print(f'[+] Messaged posted to Twitter')
    except tweepy.error.TweepError as e:
        print(f'Your tweepy error is listed below!\n{e}')
    

# post_to_twitter()


