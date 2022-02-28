import os
print(os.getcwd())
from codification_commas import insertar_comillas
from codification_spaces import insertar_tags
from decodification_commas import retrieve_msg_commas
from decodification_spaces import retrieve_msg_spaces



def msg2lbits(msg):
    # convert message in list of bytes
    byte_list = [bin(byte)[2:].zfill(8) for byte in bytearray(msg, "utf8")]
    # conver list of bytes in list of bits
    mbits = [bit for byte in byte_list for bit in byte]
    return mbits




msg = "stegoa"
mbits = msg2lbits(msg)

print("".join(mbits))
with open(os.getcwd()+"/stego/tempResponseAlejandroCommas.html") as fd:
    content = fd.read()

hlines = content.splitlines()
newhtml = []
for line in hlines:
    newline = insertar_tags(line, mbits)
    newhtml.append(newline)

print("\n".join(newhtml))

# decodification
msg = []
for line in newhtml:
    tmp = retrieve_msg_spaces(line)
    if(tmp is not None):
        msg += tmp

print("".join(msg))
