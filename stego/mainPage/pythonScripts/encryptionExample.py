import sslcrypto
from Crypto.Cipher import ARC4
from Crypto.Hash import SHA
from Crypto.Random import get_random_bytes


msg = b'stego message'

# generate session key of 160 bits
random = get_random_bytes(16)
session_key = SHA.new(random).digest() # 160 bits key length

# cipher with session key
cipher = ARC4.new(session_key)
encmsg = cipher.encrypt(msg)
# print("MSG:", len(msg), msg)
# print("CIPHERMESSAGE:", len(encmsg), encmsg)

# GENERATE SESSION KEY OF 160 BITS
random = get_random_bytes(16)
session_key = SHA.new(random).digest() # 160 bits key length

# Create curve object, generate private and public keys
curve = sslcrypto.ecc.get_curve("secp192k1")
private_key = curve.new_private_key(is_compressed=True)
public_key = curve.private_to_public(private_key)

ALGORITHM = "aes-128-cbc"
print(type(session_key), len(session_key), session_key)
# Encrypt session key
enckey = curve.encrypt(session_key, public_key, algo=ALGORITHM)

print(type(enckey), len(enckey), enckey)

# Decrypt
deckey =  curve.decrypt(enckey, private_key, algo=ALGORITHM)
print(type(deckey), len(deckey), deckey)

assert deckey == session_key
