import requests
import json

host_url = 'http://127.0.0.1:5849'
response_code = requests.get(host_url)
print('The response for this GET request is')
print(response_code)
response_result = (json.dumps(response_code.json(),indent=4))
print(response_result)