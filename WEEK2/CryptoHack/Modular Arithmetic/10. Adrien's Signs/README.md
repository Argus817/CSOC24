# Adrien's Signs

## Description

Adrien's been looking at ways to encrypt his messages with the help of 
symbols and minus signs. Can you find a way to recover the flag?  

**Challenge files:**  

- [source.py](./source.py)  
- [output.txt](./output.txt)

#### Attachments: [`source.py`](./source.py) and [`output.txt`](./output.txt)

## Solution

We are given a python script [`source.py`](./source.py) and a text file [`output.txt`](./output.txt) which was generated from the python script.

```python
from random import randint

a = 288260533169915
p = 1007621497415251

FLAG = b'crypto{????????????????????}'


def encrypt_flag(flag):
    ciphertext = []
    plaintext = ''.join([bin(i)[2:].zfill(8) for i in flag])
    for b in plaintext:
        e = randint(1, p)
        n = pow(a, e, p)
        if b == '1':
            ciphertext.append(n)
        else:
            n = -n % p
            ciphertext.append(n)
    return ciphertext


print(encrypt_flag(FLAG))
```

On analysing this script, we are given a prime `p` and a number `a` which turns out to be a Quadratic Residue. A random exponent `e` is generated and $n = a^e\ mod\ p$. The binary form of the flag is iterated through and if the digit is 1, `n` is appended to the list, else `-n % p` is appended. 

Since `a` is a Quadratic Residue, $n = a^e\ mod\ p$ would also be a Quadratic Residue for any `e`. Hence if the number in the output is a Quadratic Residue, the binary digit would be `1` else `0`.

Complete solution is given in [`solve.py`](./solve.py).

```bash
$ python3 solve.py
crypto{p4tterns_1n_re5idu3s}
```

## Answer

`crypto{p4tterns_1n_re5idu3s}`
