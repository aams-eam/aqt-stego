import requests
import html
from attPosition import decode_line

if (True):
    payload = {'pass': '1234'}
    r = requests.get("http://127.0.0.1:8000/shop", params=payload)
else:
    r = requests.get('http://127.0.0.1:8000/shop')

html_lines = html.unescape(r.text).splitlines()

totalbits = []
for line in html_lines:
    bits_part = decode_line(line)
    if(not bits_part==None):
        totalbits = totalbits + bits_part

print(totalbits)