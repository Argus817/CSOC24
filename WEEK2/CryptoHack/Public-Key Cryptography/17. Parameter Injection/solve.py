from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
from pwn import remote
from json import loads
from random import randint

host = 'socket.cryptohack.org' 
port = 13371

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

data = {}
target = remote(host,port)
target.recvuntil(b'Alice: ')
alice_key = target.recvuntil(b'}')
data.update(loads(alice_key.decode()))

p = int(data['p'][2:], base=16)
g = int(data['g'][2:], base=16)
A = int(data['A'][2:], base=16)

target.recvuntil(b'to Bob: ')
target.sendline(alice_key)

target.recvuntil(b'from Bob: ')
bob_key = target.recvuntil(b'}')
b = randint(1,p-1)
B = pow(g,b,p)

target.recvuntil(b'to Alice: ')
target.sendline(b'{'+f'"B": "{hex(B)}"'.encode()+b'}')

target.recvuntil(b'from Alice: ')
data.update(loads(target.recvuntil(b'}').decode()))

target.close()

iv = data['iv']
ct = data['encrypted_flag']

shared_secret = pow(A,b,p)
print(decrypt_flag(shared_secret,iv,ct))
