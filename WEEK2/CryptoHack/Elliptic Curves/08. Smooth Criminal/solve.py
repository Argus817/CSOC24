from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import hashlib
from sage.all import *

def decrypt_flag(shared_secret, data):
    IV = bytes.fromhex(data['iv'])
    CT = bytes.fromhex(data['encrypted_flag'])
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    KEY = sha1.digest()[:16]
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    PT = unpad(cipher.decrypt(CT), 16)
    return PT

p = 310717010502520989590157367261876774703
a = 2
b = 3

F = GF(p)
E = EllipticCurve(F, [a,b])

g_x = 179210853392303317793440285562762725654
g_y = 105268671499942631758568591033409611165
G = E(g_x, g_y)

Ax=280810182131414898730378982766101210916
Ay=291506490768054478159835604632710368904
A = E(Ax, Ay)

b_x = 272640099140026426377756188075937988094
b_y = 51062462309521034358726608268084433317
B = E(b_x, b_y)

data = {'iv': '07e2628b590095a5e332d397b8a59aa7', 'encrypted_flag': '8220b7c47b36777a737f5ef9caa2814cf20c1c1ef496ec21a9b4833da24a008d0870d3ac3a6ad80065c138a2ed6136af'}

nA = G.discrete_log(A)
S = nA*B
print(decrypt_flag(int(S.xy()[0]), data))
