import requests
from json import loads
from binascii import hexlify, unhexlify
from pwn import xor

bytesplit = lambda b,n: [b[i:i+n] for i in range(0,len(b),n)]

url = "https://aes.cryptohack.org/symmetry/"
encrypt = lambda pt,iv : unhexlify(loads(requests.get(url+"encrypt/"+hexlify(pt).decode()+"/"+hexlify(iv).decode()+"/").text)["ciphertext"].encode())

encrypt_flag = lambda : unhexlify(loads(requests.get(url+"encrypt_flag/").text)["ciphertext"].encode())

recvd = encrypt_flag()
iv = recvd[:16]
ct = recvd[16:]

recvd = encrypt(b"\x00"*len(ct),iv)
islist = bytesplit(recvd,16)
ctlist = bytesplit(ct,16)

ptlist = [xor(x,y) for x,y in zip(islist,ctlist)]
pt = b"".join(ptlist)
print(pt)
