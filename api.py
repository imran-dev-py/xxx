import requests, json 

BASE_URL = 'http://127.0.0.1:8000'

def get_request(id=None):
    data = {}
    if data is not None:
        data['id'] = id 

    URL = f'{BASE_URL}/api/'
    response = requests.get(URL, data = json.dumps(data)).json()
    print(response)

get_request()

def post_request(id=None):
    data = {
        'unique_no': 1290,
        'name': 'Sunny Deol',
        'net_worth': 25800,
        'address': 'Mumbai, India'
    }
    
    URL = f'{BASE_URL}/api/'
    response = requests.post(URL, data = json.dumps(data))
    print(response.json())
    print(response.text) # Forbidden (CSRF cookie not set...)

# post_request()

def put_request(id=None):
    data = {
        'id': id,
        'net_worth': 45000,
        'name': 'Sunny Deol'
    }
    
    URL = f'{BASE_URL}/api/'
    response = requests.put(URL, data = json.dumps(data))
    # if response.status_code == request.codes.ok:
    print(response.json())
    print(response.text) # {'key': 'value'}

# put_request(6)

def delete_request(id=None):
    data = {
        'id': id,
    }
    
    URL = f'{BASE_URL}/api/'
    response = requests.delete(URL, data = json.dumps(data)).json()
    print(response)

# delete_request(1)