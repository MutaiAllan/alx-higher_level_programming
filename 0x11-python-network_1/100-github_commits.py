#!/usr/bin/python3
"""
Lists 10 most recent commits of a repo of a given user
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits"\
            .format(sys.argv[2], sys.argv[1])
    r = requests.get(url)
    commits = r.json()
    try:
        for x in range(10):
            print("{}: {}".format(commits[x].get("sha"),
                                  commits[x].get("commit")
                                  .get("author").get("name")))
    except IndexError:
        pass
