from binascii import hexlify,unhexlify
import requests
from json import loads
from pwn import xor

url = "https://aes.cryptohack.org/bean_counter/"
encrypt = lambda : unhexlify(loads(requests.get(url+"encrypt/").text)["encrypted"])

pngsig = unhexlify(b"89504e470d0a1a0a0000000d49484452")
ct = encrypt()

keystream = xor(pngsig, ct[:16])

pt = b''
for i in range(0,len(ct),16):
    pt += xor(keystream,ct[i:i+16])
with open('bean_flag.png','wb') as f:
    f.write(pt)
    print("bean_flag.png created")
