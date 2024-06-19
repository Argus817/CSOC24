# ECB CBC WTF

Here you can encrypt in CBC but only decrypt in ECB. That shouldn't be a weakness because they're different modes... right?  

Play at [ECB CBC WTF](https://aes.cryptohack.org/ecbcbcwtf)

## Description

Here you can encrypt in CBC but only decrypt in ECB. That shouldn't be a weakness because they're different modes... right?

![diagram](https://aes.cryptohack.org/static/img/CBC_encryption.svg)

##### Help

This page offers a convenient way for you to interact with the challenge functions. You can also use GET requests to send and receive data directly from the listed routes/endpoints if you wish. For more information see the [FAQ](https://cryptohack.org/faq#blockciphers).

Your aim is to recover the `FLAG` value. Once you have it, submit it on the [CryptoHack Symmetric Ciphers page](https://cryptohack.org/challenges/aes).

### Source

```python
from Crypto.Cipher import AES


KEY = ?
FLAG = ?


@chal.route('/ecbcbcwtf/decrypt/<ciphertext>/')
def decrypt(ciphertext):
    ciphertext = bytes.fromhex(ciphertext)

    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


@chal.route('/ecbcbcwtf/encrypt_flag/')
def encrypt_flag():
    iv = os.urandom(16)

    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(FLAG.encode())
    ciphertext = iv.hex() + encrypted.hex()

    return {"ciphertext": ciphertext}
```

## Solution

The source code has two functions `encrypt_flag` and `decrypt`. The `encrypt_flag` function generates a random initialisation vector `iv` and uses it and an unknown key in CBC mode to encrypt a flag and returns the `iv` and encrypted flag. The `iv` is the first 16 bytes of the returned ciphertext and the rest is the flag. On the other hand, the `decrypt` function decrypts any valid ciphertext using the same key in ECB mode.

Since CBC mode is a combination of ECB mode and XORing of plaintexts with the previous ciphertext, decryption is made simple because we have all the necessary data required to decrypt even without knowing the key. To do this, each ciphertext block of the flag can be fed to the ECB decryption algorithm which will give us an intermediate state `IS` that was obtained after XORing plaintext blocks with previous ciphertext blocks during encryption. Hence we can XOR that `IS` with the previous ciphertext block to obtain the corresponding plaintext.

> **Note:** For the first ciphertext block, once we have the intermediate state, it will be XORed with the `iv`.

Complete solution in [`solve.py`](./solve.py).

```bash
$ python3 solve.py
crypto{3cb_5uck5_4v01d_17_!!!!!}
```

## Answer

`crypto{3cb_5uck5_4v01d_17_!!!!!}`
