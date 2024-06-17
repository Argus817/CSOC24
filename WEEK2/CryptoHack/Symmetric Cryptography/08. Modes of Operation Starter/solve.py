import requests
import hashlib
from binascii import hexlify,unhexlify

url = "https://aes.cryptohack.org/block_cipher_starter/"

encrypt_flag = lambda : unhexlify(eval(requests.get(url+"encrypt_flag/").text)["ciphertext"].encode())
decrypt = lambda ciphertext, password_hash : unhexlify(eval(requests.get(url+"decrypt/"+hexlify(ciphertext).decode()+'/'+hexlify(password_hash).decode()+'/').text)["plaintext"].encode())

print(decrypt(encrypt_flag(), hashlib.md5("keyword".encode()).digest()))
