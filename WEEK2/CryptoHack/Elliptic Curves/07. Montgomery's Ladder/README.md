# Montgomery's Ladder

## Description

This category is filled with insecure implementations of elliptic curve cryptography. Picking bad curves leads to broken protocols and fun puzzles, but private keys can be extracted from devices even when the curves picked are safe!  

One technique to learn private information is through side channel analysis. At a high level, a system performing operations with a secret can leak information about the secret through data such as the time taken, or work done by the circuit.

Timing attacks against ECDSA signing can leak information about the nonce, which together with sophisticated attacks like [LadderLeak](https://eprint.iacr.org/2020/615.pdf) can be lethal for the protocol. To protect against this, a lot of work has been done to make scalar multiplication of points on an elliptic curve to run in constant time.  

A key component of constant time algorithms for scalar multiplication for points on elliptic curves are based on Montgomery's Ladder. In this challenge, the aim is to implement the most basic version of this: Montgomery’s binary algorithm in the group E(Fp).  

**Montgomery’s binary algorithm in the group $E(F_p)$**  

Input: $P$ in $E(F_p)$ and an l-bit integer $k = Σ 2^i k_i$ where $k_{l-1} = 1$<br>Output: [k]P in $E(F_p)$  

1. Set $(R_0, R_1)$ to (P, [2]P)  
2. for $i = l - 2$ down to $0$ do  
3.     If $k_i = 0$ then  
4.         Set $(R_0, R_1)$ to $([2]R_0, R_0 + R_1)$  
5.     Else:  
6.         Set $(R_0, R_1)$ to $(R_0 + R_1, [2]R_1)$  
7. Return $R_0$  

> At a high level, notice that regardless of the bit of k, we perform both a doubling and an addition operation for each step. Compare this to the double and add algorithm we gave in the starter challenges. There are a couple obvious problems within here still: the number of steps taken leaks the bit length of k and there's an if statement, which could leak data on the bit structure of k due to branching. For the interested learner, we recommend improving your algorithm to match Alg. 8 in this resource: [Montgomery curves and their arithmetic](https://eprint.iacr.org/2017/212.pdf).  

We will work with the following elliptic curve, and prime:  

$E: Y^2 = X^3 + 486662X^2 + X$, $p: 2^{255} - 19$  

Using the above curve, and the generator point with `G.x = 9`, find the x-coordinate (decimal representation) of point `Q = [0x1337c0decafe] G` by implementing the above algorithm.  

This curve is in Montgomery form, rather than Weierstrass like many of the curves in these challenges. Although this curve can be mapped to Weierstrass form and old doubling and addition formula can be reused, we recommend working directly with the formula for Montgomery curves: $By^2 = x^3 + Ax^2 + x$. To encourage this, we give the addition and doubling formulas for the curve in affine coordinates. Please see [Montgomery curves and the Montgomery ladder](https://eprint.iacr.org/2017/293.pdf) for a beautiful and fast set of formula in projective coordinates.  

**Addition formula for Montgomery Curve (Affine)**  

Input: $P$, $Q$ in $E(F_p)$ with $P$ != $Q$<br>Output: $R = (P + Q)$ in $E(F_p)$  

$α = (y_2 - y_1) / (x_2 - x_1 )$<br>$x_3 = Bα^2 - A - x_1 - x_2$<br>$y_3 = α(x_1 - x_3) - y_1$  

**Doubling formula for Montgomery Curve (Affine)**  

Input: $P$ in $E(F_p)$<br>Output: $R = [2]P$ in $E(F_p)$  

$α = (3{x_1}^2 + 2Ax_1 + 1) / (2By_1)$  
$x_3 = Bα^2 - A - 2x_1$  
$y_3 = α(x_1 - x_3) - y_1$  

Note that all operations are performed `mod p`  

For a general overview of Montgomery's ladder, we recommend: [Montgomery curves and the Montgomery ladder](https://eprint.iacr.org/2017/293.pdf). For a clean algorithm to implement, we recommend Alg. 4 `LADDER` in [Montgomery curves and their arithmetic](https://eprint.iacr.org/2017/212.pdf) together with Alg. 1 `xADD` and Alg. 2 `xDBL`.

## Solution

We are given a Montgomery Curve $E(F_p)$, a generator point $G$, and a number `n = 0x1337c0decafe`, the objective is to find $Q$ such that $Q = nG$ on the curve. Complete algorithms for addition and multiplication are given in the description and are implemented in the solution.

Complete solution is given in [`solve.py`](./solve.py).

```bash
$ python3 solve.py
crypto{49231350462786016064336756977412654793383964726771892982507420921563002378152}
```

## Answer

`crypto{49231350462786016064336756977412654793383964726771892982507420921563002378152}`
