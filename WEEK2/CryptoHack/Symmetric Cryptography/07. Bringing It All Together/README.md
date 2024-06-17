# Bringing It All Together

## Description

Apart from the **KeyExpansion** phase, we've sketched out all the components of AES. We've shown how *SubBytes* provides confusion and *ShiftRows* and *MixColumns* provide diffusion, and how these two properties work together to repeatedly circulate non-linear transformations over the state. Finally, *AddRoundKey* seeds the key into this substitution-permutation network, making the cipher a keyed permutation.  

Decryption involves performing the steps described in the "Structure of AES" challenge in reverse, applying the inverse operations. Note that the KeyExpansion still needs to be run first, and the round keys will be used in reverse order. *AddRoundKey* and its inverse are identical as XOR has the self-inverse property.  

We've provided the key expansion code, and ciphertext that's been properly encrypted by AES-128. Copy in all the building blocks you've coded so far, and complete the `decrypt` function that implements the steps shown in the diagram. The decrypted plaintext is the flag.  

Yes, you can cheat on this challenge, but where's the fun in that?  

The code used in these exercises has been taken from Bo Zhu's super simple Python AES implementation, so we've reproduced the license here.  

**Challenge files:**  

- [aes_decrypt.py](./aes_decrypt.py)  
- [LICENSE](./LICENSE)  

**Resources:**  

- [Rolling your own crypto: Everything you need to build AES from scratch](https://github.com/francisrstokes/githublog/blob/main/2022/6/15/rolling-your-own-crypto-aes.md)

![diagram](https://cryptohack.org/static/img/aes/Structure2.png)

#### Attachments: [`aes_decrypt.py`](./aes_decrypt.py)

## Solution

We are given a python script [`aes_decrypt.py`](./aes_decrypt.py) which has a completed KeyExpansion function and an incomplete Decrypt function. The Decrypt function is simple enough to fill after looking at the diagram given. The required functions have already been worked out in previous challenges.

Complete solution is given in [`solve.py`](./solve.py).

```bash
$ python3 solve.py
b'crypto{MYAES128}'
```

## Answer

`crypto{MYAES128}`
