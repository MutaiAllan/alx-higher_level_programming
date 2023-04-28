#!/usr/bin/python3
"""
Sends a request to the URL and it takes, displays the body of the response.
"""
import sys
from urllib import request, error


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('UTF-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
