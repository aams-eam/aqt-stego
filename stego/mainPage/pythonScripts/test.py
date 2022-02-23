msg = "Esto es un mensaje cualquiera"
msglen = len(msg)
print(msglen)

# byte_list = [bin(byte)[2:].zfill(16) for byte in bytearray(msglen)]
# print(byte_list)
# # conver list of bytes in list of bits
# mbits = [bit for byte in byte_list for bit in byte]
# print(mbits)


x = "{0:b}".format(29).zfill(16)
print(x)
