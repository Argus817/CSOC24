from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
from pwn import remote
import json
from sage.all import *

host = 'socket.cryptohack.org'
port = 13379

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

target = remote(host,port)
data = dict()

target.recvuntil(b'to Bob: ')
target.sendline(b'{"supported": ["DH64"]}')
target.recvuntil(b'to Alice: ')
target.sendline(b'{"chosen": "DH64"}')

target.recvuntil(b'from Alice: ')
data.update( json.loads(target.recvuntil(b'}').decode()) )
target.recvuntil(b'from Bob: ')
data.update( json.loads(target.recvuntil(b'}').decode()) )
target.recvuntil(b'from Alice: ')
data.update( json.loads(target.recvuntil(b'}').decode()) )

target.close()

hexToInt = lambda x : int(x,base=16)
p = hexToInt(data['p'])
g = hexToInt(data['g'])
A = hexToInt(data['A'])
B = hexToInt(data['B'])
a = int(discrete_log(Mod(A,p), Mod(g,p)))
shared_secret = pow(B,a,p)

print( decrypt_flag(shared_secret, data['iv'], data['encrypted_flag']) )
