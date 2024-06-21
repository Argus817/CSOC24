# Manyprime

## Description

Using one prime factor was definitely a bad idea so I'll try using over 30 instead.  

> If it's taking forever to factorise, read up on factorisation algorithms and make sure you're using one that's optimised for this scenario.  

**Challenge files:**  

- [output.txt](output.txt)  

**Resources:**  

- [The Elliptic Curve Factorization Method](https://doc.sagemath.org/html/en/reference/interfaces/sage/interfaces/ecm.html)

## Solution

We are given a file [`output.txt`](output.txt) containing public key values `n` and `e` and ciphertext `ct`. What is interesting is that `n` has 30 prime factors. This means using an optimised prime factorisation algorithm will suffice. I used SageMath's implementation of the Elliptic Curve Method given by the function `ecm.factorise(n)`. After factorisation, finding private key and hence the decrypted flag is straightforward.

Complete solution is given in [`solve.py`](./solve.py).

```bash
$ python3 solve.py
b'crypto{700_m4ny_5m4ll_f4c70r5}'
```

## Answer

`crypto{700_m4ny_5m4ll_f4c70r5}`
