import requests

url = 'http://127.0.0.1:8000/api/get/'
data = {'id': [1, 2, 1]}
response = requests.get(url=url, params=data)
print(response.json())
