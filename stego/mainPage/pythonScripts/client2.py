import requests
import html
import re
from attPosition import decode_line as att_decode_line
from decodification_commas import retrieve_msg_commas
from decodification_commas import total_capacity as total_capacity_commas
from decodification_spaces import retrieve_msg_spaces
from decodification_spaces import total_capacity as total_capacity_spaces
from Crypto.Cipher import ARC4
import sys




### FUNCTIONS
def find_init(pattern, string):
    patterns = []
    pattern = '(?=('+pattern+'))'

    for match in re.finditer(pattern, string):
        patterns.append(match.end(1))
    return patterns


def bitstring_to_bytes(s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')


def bits2lbits(key):
    # convert message in list of bytes
    byte_list = [bin(byte)[2:].zfill(8) for byte in bytearray(key)]
    # conver list of bytes in list of bits
    kbits = [bit for byte in byte_list for bit in byte]
    return kbits

# Program to find most frequent
# element in a list
def most_frequent(vlist):
	return max(set(vlist), key = vlist.count)


# GLOBAL VARIABLES
SESSIONKEY_LEN = 160 # Number of bits of the session key
INIT_LEN = 8         # Number of bits in the init string
K1 = "ca729843da49dc89e95e57f8cb78ea2e45b58594" # Pre-shared key between client2 and the webserver
init = ['1', '0', '1', '0', '1', '0', '1', '0'] # Indicator of start of message

# CONFIGURATIONS VARIABLES
PASSWORD = "1234"


payload = {
        'pass': PASSWORD
        }
r = requests.get("http://127.0.0.1:8000/shop", params=payload)
print("STATUS_CODE: ", r.status_code)
if(r.status_code == 404):
    print("There is no secret message with that password!")
    sys.exit(0)


htmlresponse = html.unescape(r.text)
print("HTML_PAGE:\n", len(htmlresponse))
html_lines = htmlresponse.splitlines()

att_bits = []
maxbits_quote = total_capacity_commas(htmlresponse)
maxbits_tag = total_capacity_spaces(htmlresponse)


# DECODE ATT
for line in html_lines:
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
K2bytes = bytes(K2bytes)

print("K2bytes:\t", K2bytes.hex())

length_in_bytes = payload
bitlength = int.from_bytes(length_in_bytes, byteorder="big")
print("MESSAGE_LENGTH:", bitlength)


### QUOTATION MARKS
msg_commas = []
for line in html_lines:
    bits = retrieve_msg_commas(line)
    if(len(bits)>0):
        msg_commas += bits



msg_commas = "".join(msg_commas)
print(msg_commas)
patterns = find_init("".join(init), msg_commas)


#Decipher
counter = 0
all_commas = []
for patt in patterns:
    try:
        todec = msg_commas[patt:patt+bitlength]

        cipher = ARC4.new(K1bytes)
        deciphered_text_commas = cipher.decrypt(bitstring_to_bytes(todec))
        cipher = ARC4.new(K2bytes)
        deciphered_text_commas = cipher.decrypt(deciphered_text_commas)
        final = deciphered_text_commas.decode('utf-8')
        all_commas.append(final)
    except Exception as e:
        pass


print("ALL_COMMAS:", all_commas)


print()
print("SPACES TAGS")
### SPACES TAGS
msg_spaces = []
for line in html_lines:
    bits = retrieve_msg_spaces(line)
    if(len(bits)>0):
        msg_spaces += bits


msg_spaces = "".join(msg_spaces)
patterns = find_init("".join(init), msg_spaces)

#Decipher
counter = 0
all_spaces = []
for patt in patterns:
    try:
        todec = msg_spaces[patt:patt+bitlength]

        cipher = ARC4.new(K1bytes)
        deciphered_text_spaces = cipher.decrypt(bitstring_to_bytes(todec))
        cipher = ARC4.new(K2bytes)
        deciphered_text_spaces = cipher.decrypt(deciphered_text_spaces)
        final = deciphered_text_spaces.decode('utf-8')
        all_spaces.append(final)
    except Exception as e:
        pass


print("ALL_SPACES:", all_spaces)

print()
finall = all_commas+all_spaces
if(len(finall)>0):
    final_message = most_frequent(finall)
    print("FINAL MESSAGE: \"" + final_message + "\"")
else:
    print("MESSAGE COULD NOT BE DECODED!!")
