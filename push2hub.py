import argparse
from create import createRepo
from version import versionInfo
from search import searchForCompleted, project


def menu():
    parser = argparse.ArgumentParser(description="A command line tool to automatically push completed projects to github.")
    parser.add_argument("-p", "--path", dest="path", type=str, help=f'Enter the desired path that you would like to have checked.', required=False)
    parser.add_argument("-v", "--version", version=versionInfo(), help="Display version information")

    args = parser.parse_args()
    searchForCompleted(args, project)
    createRepo(project)


menu()
