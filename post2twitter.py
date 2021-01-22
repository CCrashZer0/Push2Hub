import json
import tweepy
from colorama import init 
from termcolor import colored 


def post_to_twitter():
    with open('config.json') as config:
        creds = json.load(config)

    try:
        linkText = open("link.txt", "r+")
        link = linkText.read()
    except FileNotFoundError as err:
        print(colored(f'[+] {err}', 'red'))
    
    try:
        auth = tweepy.OAuthHandler(creds["twitter_consumer_key"], creds["twitter_consumer_secret_key"])
        auth.set_access_token(creds["twitter_access_token"], creds["twitter_access_secret"])
        api = tweepy.API(auth)
        tweet_text = f"Hey yall I am working on something new. Why don't you head over to my GitHub and check it out.\n{link}\nThis tweet brought to you by push2hub\n#python #codingisfun #automation"
        api.update_status(tweet_text)
        print(colored('[+] Messaged posted to Twitter', 'green'))
    except tweepy.error.TweepError as e:
        print(colored(f'Your tweepy error is listed below!\n{e}', 'red'))
# post_to_twitter(link)


