import requests
from json import loads
from binascii import hexlify, unhexlify
from pwn import xor

url = "https://aes.cryptohack.org/ecbcbcwtf/"
ciphget = lambda : unhexlify(loads(requests.get(url+"encrypt_flag/").text)["ciphertext"].encode())
dec = lambda ct : unhexlify(loads(requests.get(url+"decrypt/"+hexlify(ct).decode()+"/").text)["plaintext"].encode())


cbcct = ciphget()
iv = cbcct[:16]
ct = cbcct[16:]

ctlist = []
for i in range(len(ct)//16):
    ctlist.append(ct[16*i: 16*(i+1)])
islist = []
for i in range(len(ctlist)):
    islist.append(dec(ctlist[i]))

pt = xor(iv,islist[0])
for i in range(len(ctlist)-1):
    pt += xor(ctlist[i], islist[i+1])

print(pt.decode())
