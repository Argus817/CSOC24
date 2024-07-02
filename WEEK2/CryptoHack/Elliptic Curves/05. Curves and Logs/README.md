# Curves and Logs

## Description

The Elliptic Curve Discrete Logarithm Problem (ECDLP) is the problem of finding an integer $n$ such that $Q = nP$.  

Like we encountered with the discrete logarithm problem, scalar multiplication of a point in $E(F_p)$ seems to be be a hard problem to undo, with the most efficient algorithm running at $O(\sqrt{p})$ time.  

This makes it a great candidate for a trapdoor function.  

Alice and Bob are talking and they want to create a shared secret so they can start encrypting their messages with some symmetric cryptographic protocol.  

Alice and Bob don't trust their connection, so they need a way to create a secret others can't replicate.  

Alice and Bob agree on a curve $E$, a prime $p$ and a generator point $G$  

In elliptic curve cryptography, it is important that the order of $G$ is prime. Constructing secure curves is complicated and it is recommended to use a preconstructed curve where a client is given the curve, the prime and the generator to use.  

Alice generates a secret random integer $n_A$ and calculates $Q_A = n_AG$  

Bob generates a secret random integer $n_B$ and calculates $Q_B = n_BG$  

Alice sends Bob $Q_A$, and Bob sends Alice $Q_B$. Due to the hardness of ECDLP, an onlooker Eve is unable to calculate $n_{A/B}$ in reasonable time.  

Alice then calculates $n_AQ_B$, and Bob calculates $n_BQ_A$.  

Due to the associativity of scalar multiplication, $S = n_AQ_B = n_BQ_A$.  

Alice and Bob can use $S$ as their shared secret.  

Using the curve, prime and generator:  

$E: Y^2 = X^3 + 497 X + 1768$, $p: 9739$, $G: (1804,5368)$  

Calculate the shared secret after Alice sends you $Q_A = (815, 3190)$, with your secret integer $n_B = 1829$.  

Generate a key by calculating the SHA1 hash of the $x$ coordinate (take the integer representation of the coordinate and cast it to a string). The flag is the hexdigest you find.  

This curve is not cryptographically secure!! We've picked a small prime for these starter challenges to keep everything fast while you learn. Cryptographically secure curves have primes of bit size ≈ 256

## Solution

Given curve $E(F_p)$, generator $G$, Alice's public key $Q_A$ and our secret integer $n_B$, the shared secret $S$ is easy to calculate as the scalar multiplication $n_BQ_A$.

Complete solution is given in [`solve.py`](./solve.py) with code implementation taken from previous challenge.

```bash
$ python3 solve.py
crypto{80e5212754a824d3a4aed185ace4f9cac0f908bf}
```

## Answer

`crypto{80e5212754a824d3a4aed185ace4f9cac0f908bf}`
