# Parameter Injection

## Description

You're in a position to not only intercept Alice and Bob's DH key exchange, but also rewrite their messages. Think about how you can play with the DH equation that they calculate, and therefore sidestep the need to crack any discrete logarithm problem.

Use the script from "Diffie-Hellman Starter 5" to decrypt the flag once you've recovered the shared secret.  

Connect at `socket.cryptohack.org 13371`

**Challenge files:**  

- [decrypt.py](decrypt.py)

## Solution

Given a `host` and `port` to connect to, the connection is like an intercept between hypothetical key exchange between Alice and Bob. We can intercept communication and even change the messages. Since Alice is the one producing the ciphertext, she must have all the necessary data needed to calculate the shared key. Hence we will pretend to be Bob, we will generate our own secret integer `b` and public key `B`. We will intercept Bob's key and replace it with our `B`. We can also calculate the shared key $A^b\ mod\ p$ using our `b` and use the methods in [`decrypt.py`](decrypt.py) to decrypt the ciphertext.

Complete solution is given in [`solve.py`](./solve.py).

```bash
$ python3 solve.py
[+] Opening connection to socket.cryptohack.org on port 13371: Done
[*] Closed connection to socket.cryptohack.org port 13371
crypto{n1c3_0n3_m4ll0ry!!!!!!!!}
```

## Answer

`crypto{n1c3_0n3_m4ll0ry!!!!!!!!}`
