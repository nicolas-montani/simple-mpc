import requests

ip =  "127.0.0.1"
def post(server, key, value):
    url = f"http://{ip}:{server}/set_value"
    data = {"index": key, "value": value}
    response = requests.post(url, data=data)
    return response.text

def get(server, key):
    url = f"http://{ip}:{server}/get_value"
    params = {"index": key}
    response = requests.get(url, params=params)
    if key == "s":
        return response.text
    else:
        return response.json()["value"]
    
def get_out(server):
    url = f"http://{ip}:{server}/out"
    response = requests.get(url)
    return response.json()["result"].split(",")
