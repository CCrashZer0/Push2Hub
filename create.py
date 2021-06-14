    import os
import json
from github import Github
from search import project



def createRepo(project):
    path = project[0]
    folder = project[1]

    with open('./config/config.json') as config:
        data = json.load(config)
    token = data['git_token']                   # Enter your access token

    g = Github(token)
    user = g.get_user()
    login = user.login
    repo = user.create_repo(folder)
    link = f'https://github.com/{login}/{folder}.git'

    fileLink = open("link.txt", "w")
    fileLink.write(link)
    fileLink.close()
    
    for i in project:
        try:
            os.chdir(path)

            f = open(".gitignore", "w+")        # Create the gitignore file
            f.write("complete.txt")             # Add the complete.txt file to the gitignore file
            f.close()                           # Close and save the changes to the file.

            os.system('git init')
            os.system('git add .')
            os.system(f'git remote add origin {link}')
            os.system('git commit -m "Initial commit made by Push2Hub"')
            os.system('git push -u origin master')

            project.remove(path)                # Remove the file path
            project.remove(folder)              # Remove teh folder name
            # print(project)
            os.remove("complete.txt")           # Remove the complete.txt file from the directory
        except OSError as e:
            print(f"Unable to created {folder} project")
            print(f'Error:\n{e}')
  
    config.close()
