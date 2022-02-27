import requests
import html
import re
from attPosition import decode_line as att_decode_line
from decodification_commas import retrieve_msg_commas
from decodification_spaces import retrieve_msg_spaces

K1 = 'ca729843da49dc89e95e57f8cb78ea2e45b58594'


if (True):
    payload = {
            'pass': '1234'
            }
    r = requests.get("http://127.0.0.1:8000/shop", params=payload)
else:
    r = requests.get('http://127.0.0.1:8000/shop')


htmlresponse = html.unescape(r.text)
html_lines = htmlresponse.splitlines()
print(htmlresponse)

att_bits = []
for line in html_lines:
    commas_bits = retrieve_msg_commas(line)
    maxbits_commas = maxbits_commas + quotation_marks_lines (line)
    spaces_bits = retrieve_msg_spaces(line)
    bits_part = att_decode_line(line)
    if(not bits_part==None):
        att_bits = att_bits + bits_part

#Key corresponds to the first 160 bits
K1bytes = bytes.fromhex(K1)
K2 = att_bits[0:160]
del att_bits[0:160]
att_bits[0:length]

#Length
quotation_marks_lines (input)





#Find init
def find_init(pattern, string):
    patterns[]
    for match in re.finditer(pattern, string):
        patterns.append(match.end())
    return patterns


counter = 0
while (True):
    #Decipher
    ciphered_text = []
    deciphered_text = []
    patterns = find_init(init, totalbits)
    pos = patterns[counter] + 1
    for i in range(pos, length):
        ciphered_text.append(totalbits[i])

    cipher = ARC4.new(K2) #Pre-shared key?
    deciphered_text = cipher.decrypt(ciphered_text)

    if (deciphered_text == "stego"):
        break
    else:
        counter = counter + 1
