from requests import post
from time import sleep
import json
import sys
from sys import argv

url = "https://techscape.ae.be/api/puzzle-cards"

cookies = {'AUTH_COOKIE': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoicGlldGVyLmZpZXJzQHN0dWRlbnQudWNsbC5iZSIsImlhdCI6MTYxMjIwODc3NX0.L6NhVAY0XSEQD-0BC2pdgYsstXvi39knbipSLahb3T0'}
headers = {"Content-Type": "application/json"}

def do_req_for_nmbr(nmbr):
    switches_bin = "{0:018b}".format(nmbr)
    switches = [(True if char == "0" else False) for char in switches_bin]
    req_data = {}
    data = {}
    data["solution"] = switches
    req_data["data"] = data
    req_data_json = json.dumps(req_data)
    res = post(url, cookies=cookies, data=req_data_json, headers=headers)
    return (res.status_code, res.text)

def do_req_with_rety(nmbr):
    retry_count = 0
    while(True):
        status, body = do_req_for_nmbr(nmbr)
        if (status == 418 and body == "Oh, come on. You can do better right?"):
            return
        elif (status == 429):
            retry_count += 1
            sleep(2 ** retry_count)
            print(f"Retry {retry_count}")
            continue
        else:
            print(f"Unkown status code and/or body: {status} {body}")
            sys.exit(1)
            
if __name__ == "__main__":
    start = int(argv[1]) if 1 < len(argv) else 0
    end = 524287

    try:
        for i in range(start, end):
            status = do_req_with_rety(i)
            print(f"{i}")
    except KeyboardInterrupt:
        sys.exit(0)
