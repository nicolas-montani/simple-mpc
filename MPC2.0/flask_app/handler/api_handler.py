# post api test to http://127.0.0.1:5000/
import requests
import json

ip =  "127.0.0.1"
def post(server, key, value):
    url = "http://" + ip + ":" + server + "/" + key
    headers = {'content-type': 'application/json'}
    payload = {key: value}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.text

def put(server, operator):
    url = "http://" + ip + ":" + server + "/z/" + operator
    response = requests.put(url)
    return response.text

def get(server, key):
    url = "http://" + ip + ":" + server + "/" + key
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    pass