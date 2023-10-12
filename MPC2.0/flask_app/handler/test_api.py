# post api test to http://127.0.0.1:5000/
import requests
import json


def post_x(value):
    url = "http://127.0.0.1:5000/x"
    payload = {"x": value}
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.text

def post_y(value):
    url = "http://127.0.0.1:5000/y"
    payload = {"y": value}
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.text

def post_z(value):
    url = "http://127.0.0.1:5000/z"
    payload = {"z": value}
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.text

def get_x():
    url = "http://127.0.0.1:5000/x"
    response = requests.get(url)
    return response.text

def get_y():
    url = "http://127.0.0.1:5000/y"
    response = requests.get(url)
    return response.text

def get_xy():
    url = "http://127.0.0.1:5000/xy"
    response = requests.get(url)
    return response.text

def get_minus():
    url = "http://127.0.0.1:5000/z/minus"
    response = requests.get(url)
    return response.text

def get_plus():
    url = "http://127.0.0.1:5000/z/plus"
    response = requests.get(url)
    return response.text

def get_times():
    url = "http://127.0.0.1:5000/z/times"
    response = requests.get(url)
    return response.text

def get_divide():
    url = "http://127.0.0.1:5000/z/divide"
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    print("post x = " + post_x(10)) # {"x": 10} )
    #print("post y = " + post_y(20)) # {"y": 20} )
    #print("x & y = " + get_xy()) # {"x": 10, "y": 20} )
    #print("x + y = " + get_plus()) # {"z": 30} )
    print("x * y = " + get_times()) # {"z": 200} )
    #print("x - y = " + get_minus()) # {"z": -10} )
    #print("x / y = " + get_divide()) # {"z": 0.5} )
    print(post_z(30))
