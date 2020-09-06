import os
from github import Github
from search import project

path = project[0]
folder = project[1]

token = ""                    # Enter your access token

g = Github(token)
user = g.get_user()
login = user.login
repo = user.create_repo(folder)

def createRepo(token, login, folder, project):
    for i in project:
        try:
            os.chdir(path)

            f = open(".gitignore","w+")         # Create the gitignore file
            f.write("complete.txt")             # Add the complete.txt file to the gitignore file
            f.close()                           # Close and save the changes to the file.

            os.system('git init')
            os.system('git add .')
            os.system(f'git remote add origin https://github.com/{login}/{folder}.git')
            os.system('git commit -m "Initial commit made by Push2Hub"')
            os.system('git push -u origin master')

            project.remove(path)                # Remove the file path
            project.remove(folder)              # Remove teh folder name
            # print(project)
            os.remove("complete.txt")           # Remove the complete.txt file from the directory
        except OSError as e:
            print(f"Unable to created {folder} project")
            print(f'Error:\n{e}')

createRepo(token, login, folder, project)
