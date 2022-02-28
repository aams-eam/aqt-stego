import os
print(os.getcwd())
from codification_commas import insertar_comillas
from codification_spaces import insertar_tags
from decodification_commas import retrieve_msg_commas
from decodification_spaces import retrieve_msg_spaces
from decodification_commas import total_capacity as quot_total_capacity
from decodification_spaces import total_capacity as space_total_capacity



def msg2lbits(msg):
    # convert message in list of bytes
    byte_list = [bin(byte)[2:].zfill(8) for byte in bytearray(msg, "utf8")]
    # conver list of bytes in list of bits
    mbits = [bit for byte in byte_list for bit in byte]
    return mbits




msg = "asf"
mbits = msg2lbits(msg)


print("".join(mbits))
with open(os.getcwd()+"/stego/responseContent.html") as fd:
    content = fd.read()


maxbits_quote = quot_total_capacity(content) # capacity of space encoding
maxbits_tag = space_total_capacity(content) # capacity of quotes encoding

print(maxbits_quote)
print(maxbits_tag)


# hlines = content.splitlines()
# newhtml = []
# for line in hlines:
#     newline = insertar_tags(line, mbits)
#     newhtml.append(newline)
#
# print("\n".join(newhtml))
#
# # decodification
# msg = []
# for line in newhtml:
#     tmp = retrieve_msg_spaces(line)
#     if(tmp is not None):
#         msg += tmp
#
# print("".join(msg))
