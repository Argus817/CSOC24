from binascii import unhexlify
from pwn import xor

data = unhexlify(b"73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
for i in range(256):
    value = xor( data, chr(i).encode()*len(data) )
    if b"crypto{" in value:
        print(value)
        break
