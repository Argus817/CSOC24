import requests
from json import loads
from binascii import hexlify

url = "https://aes.cryptohack.org/ecb_oracle/encrypt/"
enc = lambda pt : loads(requests.get(url+hexlify(pt).decode()+'/').text.strip())["ciphertext"]

flag = ""
b=1
while 32-len(flag)!=0 and b==1:
    ct = enc(b'A'*(32-len(flag)-1))[:64]

    for i in range(256):
        recvd = enc(b'A'*(32-len(flag)-1)+flag.encode()+bytes([i]))[:64]
        if recvd==ct:
            flag += chr(i)
            if chr(i)=='}':
                b=0
            break
    print(f"flag = {flag}")
