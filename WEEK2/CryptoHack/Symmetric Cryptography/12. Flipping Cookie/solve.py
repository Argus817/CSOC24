import requests
from json import loads
from binascii import hexlify, unhexlify
from Crypto.Util.Padding import pad, unpad
from pwn import xor
from datetime import datetime, timedelta

BS = 16

url = "https://aes.cryptohack.org/flipping_cookie/"
get_cookie = lambda : unhexlify(loads(requests.get(url+"get_cookie/").text)["cookie"].encode())
check_admin = lambda cookie, iv : loads(requests.get(url+"check_admin/"+hexlify(cookie).decode()+"/"+hexlify(iv).decode()+'/').text)["flag"].encode()

iv_ciph = get_cookie()
IV = iv_ciph[:BS]
CT = iv_ciph[BS:]

expires_at = (datetime.today() + timedelta(days=1)).strftime("%s")
PT0 = pad(f"admin=False;expiry={expires_at}".encode(),16)
PT = pad(f"admin=True; expiry={expires_at}".encode(),16)

PT0 = PT0[:16]
PT = PT[:16]

IS0 = xor(IV, PT0)
newIV = xor(IS0, PT)
print(check_admin(CT, newIV))
