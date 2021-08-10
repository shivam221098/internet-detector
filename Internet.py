import requests
import datetime

flag = None
while True:
    try:
        r = requests.get("https://www.google.com")
        if flag != 0:
            print("Internet available from ", datetime.datetime.now().time())
            flag = 0
    except requests.exceptions.ConnectionError:
        if flag != 1:
            print("Internet not available from ", datetime.datetime.now().time())
            flag = 1
