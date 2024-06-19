import requests
from json import loads
from binascii import hexlify,unhexlify

url = "https://aes.cryptohack.org/block_cipher_starter/"

encrypt_flag = lambda : unhexlify(loads(requests.get(url+'encrypt_flag/').text)["ciphertext"].encode())
decrypt = lambda ciphertext : unhexlify(loads(requests.get(f"{url}decrypt/{hexlify(ciphertext).decode()}/").text)['plaintext'].encode())

print(decrypt(encrypt_flag()))
