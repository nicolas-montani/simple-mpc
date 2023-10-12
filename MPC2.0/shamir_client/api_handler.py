import requests
import json


ip =  "127.0.0.1"
def post(server, key, value):
    url = "http://" + ip + ":" + server + "/" + key
    headers = {'content-type': 'application/json'}
    payload = {key: value}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.text

def create_serverlist_array():
    serverlist = []
    with open("Shamir_client/database/serverlist.txt", "r") as f:
        for line in f:
            serverlist.append(line.strip())
    return serverlist

def get(server, key):
    url = "http://" + ip + ":" + server + "/" + key
    response = requests.get(url)
    return response.json()[key]
