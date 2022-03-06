import requests

# CONFIGURATION VARIABLES
MESSAGE = "stego"
PASSWORD = "1234"
payload = {'msg': MESSAGE, 'pass': PASSWORD}
r = requests.post("http://127.0.0.1:8000/shop", data=payload)
print(r.status_code)
