# Efficient Exchange

## Description

Alice and Bob are looking at the Elliptic Curve Discrete Logarithm Problem and thinking about the data they send.  

They want to try and keep their data transfer as efficient as possible and realise that sending both the `x` and `y` coordinate of their public key isn't necessary.  

As long as Alice and Bob agree on the curve parameters, there are only ever two possible values of `y` for a given `x`.  

In fact, given *either* of the values of `y` permissible from the value `x` they receive, the `x` coordinate of their shared secret will be the same.  

> For these challenges, we have used a prime `p ≡ 3 mod 4`, which will help you find `y` from `y2`.  

Using the curve, prime and generator:  

$E: Y^2 = X^3 + 497 X + 1768$, $p: 9739$, $G: (1804,5368)$  

Calculate the shared secret after Alice sends you $Q_x = 4726$, with your secret integer $n_B = 6534$.  

Use the [`decrypt.py`](decrypt.py) file to decode the flag  

`{'iv': 'cd9da9f1c60925922377ea952afc212c', 'encrypted_flag': 'febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8'}`  

> You can specifiy which of the two possible values your public `y` coordinate has taken by sending only one bit. Try and think about how you could do this. How are the two y values related to each other?  

**Challenge files:**  

- [decrypt.py](decrypt.py)

## Solution

Given curve $E(F_p)$, generator $G$, our secret integer $n_B$ and only $x$-coordinate of Alice's public key. Since the prime given is equivalent to $3\ mod\ 4$, we can easily find square root of $y^2$ obtained from the curve equation by powering the value obtained to $(p+1)/4$ in mod $p$. Curve implementation is taken from previous challenges.

Complete solution is given in [`solve.py`](./solve.py).

```bash
$ python3 solve.py
crypto{3ff1c1ent_k3y_3xch4ng3}
```

## Answer

`crypto{3ff1c1ent_k3y_3xch4ng3}`
