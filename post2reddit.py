import json
import praw


def post_to_reddit():
    credentials = './config/config.json'
    with open(credentials) as f:
        creds = json.load(f)

    reddit = praw.Reddit(client_id=creds['reddit_id'],
                        client_secret=creds['reddit_secret'],
                        user_agent=creds['reddit_user_agent'],
                        redirect_uri=creds['reddit_redirect_uri'],
                        refresh_token=creds['reddit_refresh_token'])
    subr = ['pythonsandlot','learnpython'] # Choose your subreddit
    for i in subr:
        subreddit = reddit.subreddit(i) # Initialize the subreddit to a variable
        title = 'Just Made My first Post on Reddit Using Python.'
        selftext = '''
        I am learning how to use the Reddit API with Python using the PRAW wrapper.
        By following the tutorial on https://www.jcchouinard.com/post-on-reddit-api-with-python-praw/
        This post was uploaded from my Python Script
        '''
        subreddit.submit(title,selftext=selftext)


# post_to_reddit()