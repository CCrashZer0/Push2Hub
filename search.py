import os


global project
project = []


def searchForCompleted(args, project):

    exclude = set([".git", "images"])

    for root, dirs, files in os.walk(args.path, topdown=True):
        [dirs.remove(d) for d in list(dirs) if d in exclude]
        for i in files:
            if i.endswith('complete.txt'):
                project.append(root)
                project.append(os.path.basename(os.path.normpath(root)))
    return project
