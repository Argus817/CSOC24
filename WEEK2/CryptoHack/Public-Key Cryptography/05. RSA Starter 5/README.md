# RSA Starter 5

## Description

I've encrypted a secret number for your eyes only using your public key parameters:

`N = 882564595536224140639625987659416029426239230804614613279163`  

`e = 65537`  

Use the private key that you found for these parameters in the previous challenge to decrypt this ciphertext:  

`c = 77578995801157823671636298847186723593814843845525223303932`

## Solution

Given `N`, `e`, `c` and `p`, `q` and `d` from previous challenge, decryption is made easy and plaintext will be calculated as $p = c^d\ mod\ N$ or `p = pow(c,d,N)`.

Complete solution is given in [`solve.py`](./solve.py).

```bash
$ python3 solve.py
Plaintext = 13371337
```

## Answer

`13371337`
