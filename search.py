import os
import sys

path = "E:\\CTF\\WriteUps" #\\THM"
exclude = set([".git","images"])
project = []


def search(path, exclude):
    for root, dirs, files in os.walk(path, topdown=True):
        [dirs.remove(d) for d in list(dirs) if d in exclude]
        for i in files:
            if i.endswith('complete.txt'):
                project.append(root)
                # dirName = root
                project.append(os.path.basename(os.path.normpath(root))) # Get the directory of the completed project
                # print(f"{dirName}\n{folderName}\n")
    # return f"{dirName}\n{folderName}\n"
search(path, exclude)
print(project)