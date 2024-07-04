from fastecdsa import curve,keys
from pwn import remote
from sage.all import *

host = 'socket.cryptohack.org'
port = 13382

G = curve.P256.G
priv_key = keys.gen_private_key(curve.P256)

E = EllipticCurve(GF(curve.P256.p),[curve.P256.a,curve.P256.b])
key = E(0x3B827FF5E8EA151E6E51F8D0ABF08D90F571914A595891F9998A5BD49DFA3531, 0xAB61705C502CA0F7AA127DEC096B2BBDC9BD3B4281808B3740C320810888592A)
g = key*(pow(2,-1,curve.P256.q))

assert g*2==key

target = remote(host,port)
target.recv()
target.sendline(b'{'+f'"private_key": 2, "host": "www.bing.com", "curve":"secp256r1", "generator": {[g.xy()[0], g.xy()[1]]}'.encode()+b'}')
target.recvuntil(b'about ')
print(target.recv()[:-2])
