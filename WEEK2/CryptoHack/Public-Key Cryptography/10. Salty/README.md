# Salty

## Description

Smallest exponent should be fastest, right?  

**Challenge files:**  

- [salty.py](./salty.py)  
- [output.txt](./output.txt)

## Solution

We are given a python script [`salty.py`](./salty.py) which generates [`output.txt`](./output.txt). The script is as below...

```python
#!/usr/bin/env python3

from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes

e = 1
d = -1

while d == -1:
    p = getPrime(512)
    q = getPrime(512)
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)

n = p * q

flag = b"XXXXXXXXXXXXXXXXXXXXXXX"
pt = bytes_to_long(flag)
ct = pow(pt, e, n)

print(f"n = {n}")
print(f"e = {e}")
print(f"ct = {ct}")

pt = pow(ct, d, n)
decrypted = long_to_bytes(pt)
assert decrypted == flag
```

The exponent used here is `1` so it is pretty obvious that `ct == pt`.

Complete solution is given in [`solve.py`](./solve.py).

```bash
$ python3 solve.py 
b'crypto{saltstack_fell_for_this!}'
```

## Answer

`crypto{saltstack_fell_for_this!}`
