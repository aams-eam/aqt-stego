message = "abc"
num_bits = 3

byte_list = [bin(byte)[2:].zfill(8) for byte in bytearray(message, "utf8")]
res = [bit for byte in byte_list for bit in byte]


print(res)
mbits_part = res[0:num_bits]
del res[0:num_bits]
# encode mbits_part (modify that html line)
print(res)
print()
print(mbits_part)



att_sorted = [('style', 'border:0'), ('src', 'htt4452'), ('height', '380'), ('allowfullscreen', ''), ('width', '100%'), ('frameborder', '0')]
temp = att_sorted[3][1]
print(temp=='')

x = "stringraro jeje"
print(y)


newhtml = []
# take first num_bits from the message
message = "Mensaje a codificar"
# convert message in list of bytes
byte_list = [bin(byte)[2:].zfill(8) for byte in bytearray(message, "utf8")]
# conver list of bytes in list of bits
mbits = [bit for byte in byte_list for bit in byte]
print(mbits)

print(len(['0', '1', '0', '0', '1', '1', '0', '1', '0', '1', '1', '0', '0', '1', '0', '1', '0', '1', '1', '1', '0', '1', '1', '0', '0', '1', '0', '1', '0', '1', '1', '1']))
output = [
    2,
    2,
    2,
    2,
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    6,
    6,
    6,
    6,
    0,
    0,
    0,
    0,
    3,
    3,
    3,
    3,
]
print(sum(output))
