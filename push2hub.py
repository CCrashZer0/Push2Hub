
import argparse
from create import createRepo
from version import versionInfo
from search import searchForCompleted, project


def menu():
    parser = argparse.ArgumentParser(description="A command line tool to automatically push completed projects to github.")
    parser.add_argument("-p", "--path", type=str, dest="path", help='Enter the desired path that you would like to have checked.', required=False)
    parser.add_argument('-v', '--version', action='store_true', help="shows version")

    args = parser.parse_args()

    if args.path:
        searchForCompleted(args, project)
        createRepo(project)

    if args.version:
        versionInfo()


menu()
