# Modes of Operation Starter

The previous set of challenges showed how AES performs a keyed permutation on a block of data. In practice, we need to encrypt messages much longer than a single block. A *mode of operation* describes how to use a cipher like AES on longer messages.  

All modes have serious weaknesses when used incorrectly. The challenges in this category take you to a different section of the website where you can interact with APIs and exploit those weaknesses. Get yourself acquainted with the interface and use it to take your next flag!  

Play at [Modes of Operation Starter](https://aes.cryptohack.org/block_cipher_starter)

## Description

The previous set of challenges showed how AES performs a keyed permutation on a block of data. In practice, we need to encrypt messages much longer than a single block. A *mode of operation* describes how to use a cipher like AES on longer messages.  

All modes have serious weaknesses when used incorrectly. The challenges in this category take you to a different section of the website where you can interact with APIs and exploit those weaknesses. Get yourself acquainted with the interface and use it to take your next flag!

![diagram](https://aes.cryptohack.org/static/img/ECB_encryption.svg)

#### Help

This page offers a convenient way for you to interact with the challenge functions. You can also use GET requests to send and receive data directly from the listed routes/endpoints if you wish. For more information see the [FAQ](https://cryptohack.org/faq#blockciphers).

Your aim is to recover the `FLAG` value. Once you have it, submit it on the [CryptoHack Symmetric Ciphers page](https://cryptohack.org/challenges/aes).

### Source

```python
from Crypto.Cipher import AES


KEY = ?
FLAG = ?


@chal.route('/block_cipher_starter/decrypt/<ciphertext>/')
def decrypt(ciphertext):
    ciphertext = bytes.fromhex(ciphertext)

    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


@chal.route('/block_cipher_starter/encrypt_flag/')
def encrypt_flag():
    cipher = AES.new(KEY, AES.MODE_ECB)
    encrypted = cipher.encrypt(FLAG.encode())

    return {"ciphertext": encrypted.hex()}
```

## Solution

On analysing the given source code, it is understood that the `encrypt_flag` function gives us the encrypted flag and the `decrypt` function can decrypt any ciphertext. Hence directly feeding the output of `encrypt_flag` to the `decrypt` function shall do the trick.

Complete solution is given in [`solve.py`](./solve.py).

```bash
$ python3 solve.py
b'crypto{bl0ck_c1ph3r5_4r3_f457_!}'
```

## Answer

`crypto{bl0ck_c1ph3r5_4r3_f457_!}`
