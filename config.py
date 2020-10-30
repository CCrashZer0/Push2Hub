import os
import json
import time


configData = {
'token': '',
'twitter': '',
'linkedin': ''
}


def createConfig(configData):

    f = json.dumps(configData, indent= 2)
    with open('config.json', 'w') as configFile:
        configFile.write(f)
        configFile.close()


if os.path.exists("./config.json"):
    print(f'[+] Configuration file already exists')
else:
    print(f'[+] Configuration file not located')
    createConfig(configData)
    time.sleep(2)
    print(f'[+] Creating configuration file ')