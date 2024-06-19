# Flipping Cookie

You can get a cookie for my website, but it won't help you read the flag... I think.  

Play at [Flipping Cookie](https://aes.cryptohack.org/flipping_cookie)

## Description

You can get a cookie for my website, but it won't help you read the flag... I think.

##### Help

This page offers a convenient way for you to interact with the challenge functions. You can also use GET requests to send and receive data directly from the listed routes/endpoints if you wish. For more information see the [FAQ](https://cryptohack.org/faq#blockciphers).

Your aim is to recover the `FLAG` value. Once you have it, submit it on the [CryptoHack Symmetric Ciphers page](https://cryptohack.org/challenges/aes).

### Source

```python
from Crypto.Cipher import AES
import os
from Crypto.Util.Padding import pad, unpad
from datetime import datetime, timedelta


KEY = ?
FLAG = ?


@chal.route('/flipping_cookie/check_admin/<cookie>/<iv>/')
def check_admin(cookie, iv):
    cookie = bytes.fromhex(cookie)
    iv = bytes.fromhex(iv)

    try:
        cipher = AES.new(KEY, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(cookie)
        unpadded = unpad(decrypted, 16)
    except ValueError as e:
        return {"error": str(e)}

    if b"admin=True" in unpadded.split(b";"):
        return {"flag": FLAG}
    else:
        return {"error": "Only admin can read the flag"}


@chal.route('/flipping_cookie/get_cookie/')
def get_cookie():
    expires_at = (datetime.today() + timedelta(days=1)).strftime("%s")
    cookie = f"admin=False;expiry={expires_at}".encode()

    iv = os.urandom(16)
    padded = pad(cookie, 16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(padded)
    ciphertext = iv.hex() + encrypted.hex()

    return {"cookie": ciphertext}
```

## Solution

The source code contains two functions `get_cookie` and `check_admin`. The `get_cookie` function provides us with an initialization vector `IV` and encrypted cookie representing the plaintext `admin=False;expiry=....`. The `check_admin` function checks if the input cookie decrypts to a string containing `admin=True` and returns the flag if the condition is satisfied.

All we need to do is manipulate the `IV` and the ciphertext `CT` such that the decryption process results in `admin=True`. We can't make any changes in the ciphertext as each `CT` block will be XORed with the intermediate state `IS` of the next block and so on. So we will need to make changes to the `IV`.

Using properties of XOR, `IV` is nothing but `is1`^`'admin=False;expiry=....'` where `is1` represents intermediate state of first ciphertext block. Hence the new initialisation vector `newIV` should be `IV`^'`'admin=False;expiry=....'`'^`'admin=True ;expiry=....'` .

Complete solution in [`solve.py`](./solve.py).

```bash
$ python3 solve.py
b'crypto{4u7h3n71c4710n_15_3553n714l}'
```

## Answer

`crypto{4u7h3n71c4710n_15_3553n714l}`
