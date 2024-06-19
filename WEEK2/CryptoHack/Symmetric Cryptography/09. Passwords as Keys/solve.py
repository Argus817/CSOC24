from Crypto.Cipher import AES
import requests
from json import loads
import hashlib
from binascii import hexlify,unhexlify

url = "https://aes.cryptohack.org/passwords_as_keys/"

encrypt_flag = lambda : unhexlify(loads(requests.get(url+"encrypt_flag/").text)["ciphertext"].encode())

def decrypt(ciphertext):
    with open("/usr/share/dict/words") as f:
        words = [w.strip() for w in f.readlines()]

    for word in words:
        key = hashlib.md5(word.encode()).digest()
        cipher = AES.new(key, AES.MODE_ECB)
        try:
            decrypted = cipher.decrypt(ciphertext)
            if b"crypto" not in decrypted:
                continue
            return decrypted
        except ValueError as e:
            "Wrong key"
            continue

print(decrypt(encrypt_flag()))
