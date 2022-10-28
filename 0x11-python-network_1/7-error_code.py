#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
and displays the body of the response.

-If the HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status code
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    s_code = r.status_code

    if s_code >= 400:
        print("Error code: {}".format(s_code))
    else:
        print(r.text)
