import os
import json
import time
from colorama import init 
from termcolor import colored 


configData = {
    'git_token': '',
    'bit_token': '',
    'twitter_consumer_key': '',
    'twitter_consumer_secret_key': '',
    'twitter_access_token': '',
    'twitter_access_secret': '',
    'linkedin': ''
}


def createConfig(configData):

    f = json.dumps(configData, indent=2)
    with open('config.json', 'w') as configFile:
        configFile.write(f)
        configFile.close()

init() 
if os.path.exists("./config.json"):
    print(colored('[+] Configuration file already exists', 'green'))
else:
    print(colored('[+] Configuration file not located', 'red'))
    createConfig(configData)
    time.sleep(2)
    print(colored('[+] Creating configuration file ','green'))
