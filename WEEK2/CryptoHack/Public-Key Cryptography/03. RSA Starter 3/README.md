# RSA Starter 3

## Description

RSA relies on the difficulty of the factorisation of the modulus `N`. If the primes can be found then we can calculate the [Euler totient](https://leimao.github.io/article/RSA-Algorithm/) of `N` and thus decrypt the ciphertext.  

Given `N = p*q` and two primes:  

`p = 857504083339712752489993810777`  

`q = 1029224947942998075080348647219`  

What is the totient of `N`?

## Solution

For prime factors `p` and `q` of `N = p*q`, totient of `N` is given as $\phi(N) = (p-1)(q-1)$. Hence totient of `N` is `phi = (p-1)*(q-1)`.

Complete solution given in [`solve.py`](./solve.py).

```bash

```

## Answer

`882564595536224140639625987657529300394956519977044270821168`
