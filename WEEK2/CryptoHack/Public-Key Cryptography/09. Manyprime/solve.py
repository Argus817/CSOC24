from Crypto.Util.number import long_to_bytes
from sage.all import *

def read_key_file(filename):
    values = {}
    with open(filename, 'r') as file:
        for line in file:
            key, value = line.split('=')
            values[key.strip()] = int(value.strip())
    return values

n,e,ct = tuple(read_key_file("output.txt").values())
factors = [int(i) for i in ecm.factor(n)]

phi = 1
for factor in factors:
    phi *= factor-1
d = pow(e,-1,phi)
pt = pow(ct,d,n)
print(long_to_bytes(pt))
