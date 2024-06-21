# RSA Starter 2

## Description

RSA encryption is modular exponentiation of a message with an exponent `e` and a modulus `N` which is normally a product of two primes: `N = p * q`.  

Together the exponent and modulus form an RSA "public key" `(N, e)`. The most common value for `e` is `0x10001` or `65537`.  

"Encrypt" the number `12` using the exponent `e = 65537` and the primes `p = 17` and `q = 23`. What number do you get as the ciphertext?

## Solution

Encryption of any number (plaintext) `PT` to ciphertext `CT` is simply modular exponentiation of `PT` to the power `e` mod `N` such that `e` is the public-key exponent and `N` is the public key modulus.

Complete solution given in [`solve.py`](./solve.py).

```bash
$ python3 solve.py
CT = 301
```

## Answer

`301`
