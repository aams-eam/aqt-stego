import requests
import html
from attPosition import decode_line
from attPosition import total_capacity

# CONFIGURATION
postmsg = 'stego'
postpass = '1234'
getpass = '1234'
withpass = True

payload = {'msg': postmsg, 'pass': postpass}
r = requests.post("http://127.0.0.1:8000/shop", data=payload)

if (withpass):
    payload = {'pass': getpass}
    r = requests.get("http://127.0.0.1:8000/shop", params=payload)
else:
    r = requests.get('http://127.0.0.1:8000/shop')


htmlresponse =html.unescape(r.text)
html_lines = htmlresponse.splitlines()
print(htmlresponse)

totalbits = []
for line in html_lines:
    bits_part = decode_line(line)
    if(not bits_part==None):
        totalbits = totalbits + bits_part

print(totalbits)

maxbits = total_capacity(htmlresponse)
basebits_of_len = len("{0:b}".format(maxbits))
bits_of_key = 16
redundancy = 1
init = "0001001" # algo


# find init
pos = 0

msg_length_bits = totalbits[pos:basebits_of_len]
del totalbits[pos:basebits_of_len]
msg_length = int("".join(msg_length_bits), 2)
msg = "".join(totalbits[:msg_length])
del totalbits[:msg_length]


# IS A BETTER WAY TO DECODE UTF-8 FROM STRING OF BITS ?
msg = [msg[i:i+8] for i in range(0, len(msg), 8)]
msg = "".join([chr(int(c, 2)) for c in msg])
assert msg == postmsg
