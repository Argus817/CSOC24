# Monoprime

## Description

Why is everyone so obsessed with multiplying two primes for RSA. Why not just use one?  

**Challenge files:**

- [output.txt](./output.txt)  

**Resources:**  

- [Why do we need in RSA the modulus to be product of 2 primes?](https://crypto.stackexchange.com/questions/5170/why-do-we-need-in-rsa-the-modulus-to-be-product-of-2-primes)

## Solution

We are given a file [`output.txt`](./output.txt) containing public key values `n` and `e` and ciphertext `ct`. Here, `n` is a prime and hence calculating private key modulus is made easy. It can be calculated as $d = e^{-1}\ mod\ (n-1)$. After that, decryption is done as usual.

Complete solution is given in [`solve.py`](./solve.py).

```bash
$ python3 solve.py
b'crypto{0n3_pr1m3_41n7_pr1m3_l0l}'
```

## Answer

`crypto{0n3_pr1m3_41n7_pr1m3_l0l}`
