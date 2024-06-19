# ECB Oracle

ECB is the most simple mode, with each plaintext block encrypted entirely independently. In this case, your input is prepended to the secret flag and encrypted and that's it. We don't even provide a decrypt function. Perhaps you don't need a padding oracle when you have an "ECB oracle"?  

Play at [ECB Oracle](https://aes.cryptohack.org/ecb_oracle)

## Description

ECB is the most simple mode, with each plaintext block encrypted entirely independently. In this case, your input is prepended to the secret flag and encrypted and that's it. We don't even provide a decrypt function. Perhaps you don't need a padding oracle when you have an "ECB oracle"?

![diagram](https://aes.cryptohack.org/static/img/ECB_encryption.svg)

##### Help

This page offers a convenient way for you to interact with the challenge functions. You can also use GET requests to send and receive data directly from the listed routes/endpoints if you wish. For more information see the [FAQ](https://cryptohack.org/faq#blockciphers).

Your aim is to recover the `FLAG` value. Once you have it, submit it on the [CryptoHack Symmetric Ciphers page](https://cryptohack.org/challenges/aes).

### Source

```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


KEY = ?
FLAG = ?


@chal.route('/ecb_oracle/encrypt/<plaintext>/')
def encrypt(plaintext):
    plaintext = bytes.fromhex(plaintext)

    padded = pad(plaintext + FLAG.encode(), 16)
    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        encrypted = cipher.encrypt(padded)
    except ValueError as e:
        return {"error": str(e)}

    return {"ciphertext": encrypted.hex()}
```

## Solution

From the source code, it can be deduced that the `encrypt` function appends the flag to arbitrary plaintext and returns the result after encrypting it. Since AES is a block cipher and the ECB (Electonic Code Book) mode encrypts blocks of plaintext, we can bruteforce our way by adjusting the length of plaintext that is input.

Each character needs to be brute forced, hence, we start with an initial message length of 31 (considering the flag to be at least 32 bytes long, and block size to be 16), our initial plaintext shall be `b'A'*31`. Our flag format is `crypto{.....}` and hence the first two blocks of our ciphertext shall represent `b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAc'` and the rest would be `b'rypto....'`. Now next we shall send the plaintext as `b'A'*31+chr(i).encode()` where `i` loops from 0 to 255. In this way, we will receive the ciphertext representing `b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+chr(i).encode()` and the rest will be `b'crypto...'`. Comparing the ciphertexts will give us our resultant characters.

Complete solution is given in [`solve.py`](./solve.py).

```bash
$ python3 solve.py
flag = c
flag = cr
flag = cry
flag = cryp
flag = crypt
flag = crypto
flag = crypto{
flag = crypto{p
flag = crypto{p3
flag = crypto{p3n
flag = crypto{p3n6
flag = crypto{p3n6u
flag = crypto{p3n6u1
flag = crypto{p3n6u1n
flag = crypto{p3n6u1n5
flag = crypto{p3n6u1n5_
flag = crypto{p3n6u1n5_h
flag = crypto{p3n6u1n5_h4
flag = crypto{p3n6u1n5_h47
flag = crypto{p3n6u1n5_h473
flag = crypto{p3n6u1n5_h473_
flag = crypto{p3n6u1n5_h473_3
flag = crypto{p3n6u1n5_h473_3c
flag = crypto{p3n6u1n5_h473_3cb
flag = crypto{p3n6u1n5_h473_3cb}
```

## Answer

`crypto{p3n6u1n5_h473_3cb}`
