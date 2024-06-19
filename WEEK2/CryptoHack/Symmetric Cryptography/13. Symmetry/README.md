# Symmetry

Some block cipher modes, such as OFB, CTR, or CFB, turn a block cipher into a stream cipher. The idea behind stream ciphers is to produce a pseudorandom keystream which is then XORed with the plaintext. One advantage of stream ciphers is that they can work of plaintext of arbitrary length, with no padding required.  

OFB is an obscure cipher mode, with no real benefits these days over using CTR. This challenge introduces an unusual property of OFB.  

Play at [Symmetry](https://aes.cryptohack.org/symmetry)

## Description

Some block cipher modes, such as OFB, CTR, or CFB, turn a block cipher into a stream cipher. The idea behind stream ciphers is to produce a pseudorandom keystream which is then XORed with the plaintext. One advantage of stream ciphers is that they can work of plaintext of arbitrary length, with no padding required.  

OFB is an obscure cipher mode, with no real benefits these days over using CTR. This challenge introduces an unusual property of OFB.

![diagram](https://aes.cryptohack.org/static/img/OFB_encryption.svg)

##### Help

This page offers a convenient way for you to interact with the challenge functions. You can also use GET requests to send and receive data directly from the listed routes/endpoints if you wish. For more information see the [FAQ](https://cryptohack.org/faq#blockciphers).

Your aim is to recover the `FLAG` value. Once you have it, submit it on the [CryptoHack Symmetric Ciphers page](https://cryptohack.org/challenges/aes).

### Source

```python
from Crypto.Cipher import AES


KEY = ?
FLAG = ?


@chal.route('/symmetry/encrypt/<plaintext>/<iv>/')
def encrypt(plaintext, iv):
    plaintext = bytes.fromhex(plaintext)
    iv = bytes.fromhex(iv)
    if len(iv) != 16:
        return {"error": "IV length must be 16"}

    cipher = AES.new(KEY, AES.MODE_OFB, iv)
    encrypted = cipher.encrypt(plaintext)
    ciphertext = encrypted.hex()

    return {"ciphertext": ciphertext}


@chal.route('/symmetry/encrypt_flag/')
def encrypt_flag():
    iv = os.urandom(16)

    cipher = AES.new(KEY, AES.MODE_OFB, iv)
    encrypted = cipher.encrypt(FLAG.encode())
    ciphertext = iv.hex() + encrypted.hex()

    return {"ciphertext": ciphertext}
```

## Solution

The source code gives us access to 2 functions `encrypt` and `encrypt_flag`. The `encrypt_flag` outputs the initialization vector `IV` and encrypted flag using the OFB mode. The `encrypt` function encrypts any plaintext and returns its ciphertext.

Now, looking at the Output Feedback (OFB) mode encryption in AES, we see that the `IV` is passed through the block cipher encryption to produce an intermediate state `IS` and then this state is XORed with a plaintext block to produce ciphertext. Now, this `IS` is again passed through the block cipher to produce the next `IS` which is XORed with the next plaintext block to produce the ciphertext. Now, if we set the plaintext to be full of zeroes and adjust the length, send it to the `encrypt` function, we will receive the entire stream of intermediate states. Now nothing is left secret and the flag can easily be derived using the properties of XOR.

Complete solution is given in [`solve.py`](./solve.py).

```bash
$ python3 solve.py
b'crypto{0fb_15_5ymm37r1c4l_!!!11!}'
```

## Answer

`crypto{0fb_15_5ymm37r1c4l_!!!11!}`
