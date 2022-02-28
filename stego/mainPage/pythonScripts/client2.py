import requests
import html
import re
from attPosition import decode_line as att_decode_line
from decodification_commas import retrieve_msg_commas
from decodification_commas import total_capacity as total_capacity_commas
from decodification_spaces import retrieve_msg_spaces
from decodification_spaces import total_capacity as total_capacity_spaces
from Crypto.Cipher import ARC4




### FUNCTIONS
def find_init(pattern, string):
    patterns = []
    for match in re.finditer(pattern, string):
        patterns.append(match.end())
    return patterns


def bitstring_to_bytes(s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')


def bits2lbits(key):
    # convert message in list of bytes
    byte_list = [bin(byte)[2:].zfill(8) for byte in bytearray(key)]
    # conver list of bytes in list of bits
    kbits = [bit for byte in byte_list for bit in byte]
    return kbits

SESSIONKEY_LEN = 160 # Number of bits of the session key
INIT_LEN = 8         # Number of bits in the init string
K1 = "ca729843da49dc89e95e57f8cb78ea2e45b58594" # Pre-shared key between client2 and the webserver
K2assert = "ca729843da49dc89e95e57fabc78ea2e45b58594"


if (True):
    payload = {
            'pass': '1234'
            }
    r = requests.get("http://127.0.0.1:8000/shop", params=payload)
else:
    r = requests.get('http://127.0.0.1:8000/shop')


htmlresponse = html.unescape(r.text)
html_lines = htmlresponse.splitlines()

att_bits = []
maxbits_quote = total_capacity_commas(htmlresponse)
maxbits_tag = total_capacity_spaces(htmlresponse)


for line in html_lines:
    commas_bits = retrieve_msg_commas(line)
    spaces_bits = retrieve_msg_spaces(line)
    # att_bits.append(att_decode_line(line))
    bits_part = att_decode_line(line)
    if(not bits_part==None):
        att_bits = att_bits + bits_part

att_bits = "".join(att_bits)
maxlength = len("{0:b}".format(min(maxbits_quote, maxbits_tag)))

#Key corresponds to the first 160 bits
K1bytes = bytes.fromhex(K1)
ciphered_payload = att_bits[0:SESSIONKEY_LEN+maxlength+(8 - ((SESSIONKEY_LEN+maxlength)%8))]

cipher = ARC4.new(K1bytes)
ciphered_payload_bytes = bitstring_to_bytes(ciphered_payload)

payload = cipher.decrypt(ciphered_payload_bytes)
payload = bytearray(payload)
K2bytes = payload[:20]
del payload[:20]

print("K2bytes:\t", K2bytes.hex())
print("K2assert:\t", K2assert)

length_in_bytes = payload
bitlength = int.from_bytes(length_in_bytes, byteorder="big")
print(bitlength)

init = ['1', '0', '0', '1', '1', '0', '0', '0'] # Indicator of start of message

# TO-DO*** comprobar que el encode de ivan y el decode de Pablo funcionan seguidos
# TO-DO*** comprobar que el countbits de ivan y Pablo son iguales



### QUOTATION MARKS
msg_commas = []
for line in html_lines:
    bits = retrieve_msg_commas(line)
    if(len(bits)>0):
        msg_commas += bits

msg_commas = "".join(msg_commas)
print(msg_commas)
print("Total bits:", len(msg_commas)) # TO-DO*** should be the same as Django...
patterns = find_init("".join(init), msg_commas)
print("PATTERNS", patterns)
print("num_messages", len(patterns))

#Decipher
counter = 0
cipher = ARC4.new(K1bytes)

for patt in patterns:
    print(patt)


while (True):
    pos = patterns[counter] + 1
    for i in range(pos, pos+length):
        ciphered_text_commas.append(msg_commas[i])

    deciphered_text_commas = cipher.decrypt(bitstring_to_bytes("".join(ciphered_text_commas)))
    plaintext = deciphered_text_commas.decode("utf-8")

    if (plaintext == "stego"):
        break
    else:
        counter = counter + 1

























# ### SPACES
# msg_spaces = []
# for line in html_lines:
#     tmp = retrieve_msg_spaces(line)
#     if(len(tmp) > 0):
#         msg_spaces += tmp
#
# patterns = find_init(init, msg_spaces)
# #Decipher
# counter = 0
# cipher = ARC4.new(K2bytes)
#
# while (True):
#     pos = patterns[counter] + 1
#     for i in range(pos, pos+length):
#         ciphered_text_spaces.append(msg_spaces[i])
#
#     deciphered_text_spaces = cipher.decrypt(bitstring_to_bytes("".join(ciphered_text_spaces)))
#     plaintext = deciphered_text_spaces.decode("utf-8")
#
#     if (plaintext == "stego"):
#         break
#     else:
#         counter = counter + 1
