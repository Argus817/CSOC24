# Export-grade

## Description

Alice and Bob are using legacy codebases and need to negotiate parameters they both support. You've man-in-the-middled this negotiation step, and can passively observe thereafter. How are you going to ruin their day this time?  

Connect at `socket.cryptohack.org 13379`

## Solution

The connection allows us to man-in-the-middle between Alice and Bob and we can intercept and change supported and chosen legacy algorithm but not change the key values. Hence chosing only DH64 is feasible for fast calculation of discrete logarithm.

Complete solution is given in [`solve.py`](./solve.py).

```bash
$ python3 solve.py
[+] Opening connection to socket.cryptohack.org on port 13379: Done
[*] Closed connection to socket.cryptohack.org port 13379
crypto{d0wn6r4d35_4r3_d4n63r0u5}
```

## Answer

`crypto{d0wn6r4d35_4r3_d4n63r0u5}`
