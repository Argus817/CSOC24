# Scalar Multiplication

## Description

Scalar multiplication of two points is defined by repeated addition: `3P = P + P + P`.  

In the next few challenges, we will use scalar multiplication to create a shared secret over an insecure channel similarly to the Diffie-Hellman challenges.  

Taken from "An Introduction to Mathematical Cryptography", *Jeffrey Hoffstein, Jill Pipher, Joseph H. Silverman*, the following algorithm will efficently calculate scalar multiplication of a point on an elliptic curve  

> **Double and Add algorithm for the scalar multiplication of point P by n**  
> 
> Input: P in E(Fp) and an integer n > 0  
> 
> a. Set Q = P and R = O.<br>b. Loop while n > 0.<br>     c. If n ≡ 1 mod 2, set R = R + Q.<br>     d. Set Q = 2 Q and n = ⌊n/2⌋.<br>     e. If n > 0, continue with loop at Step b.<br>f. Return the point R, which equals nP.  

<br>

> This is not the most efficient algorithm, there are many interesting ways to improve this calculation up, but this will be sufficient for our work.

We will work with the following elliptic curve, and prime:  

$E: Y^2 = X^3 + 497 X + 1768$, $p: 9739$  

> You can test your algorithm by asserting: `1337 X = (1089, 6931)` for `X = (5323, 5438)`.  

Using the above curve, and the points `P = (2339, 2213)`, find the point `Q(x,y) = 7863 P` by implementing the above algorithm.  

> After calculating `Q`, substitute the coordinates into the curve. Assert that the point `Q` is in $E(F_p)$.

## Solution

Given curve $E(F_p)$ and point $P$, the objective is to find $7863P$ using the algorithm of scalar multiplication. I have used the same code from the previous challenge and added a function to overload `*` operator in the `Point` object. The scalar multiplication code is implemented in this function.

Complete solution is given in [`solve.py`](./solve.py).

```bash
$ python3 solve.py
crypto{9467,2742}
```

## Answer

`crypto{9467,2742}`
