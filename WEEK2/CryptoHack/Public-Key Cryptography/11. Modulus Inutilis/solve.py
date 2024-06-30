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

pt = int( Integer(ct)**(Integer(1)/Integer(3)) )
print(long_to_bytes(pt))
