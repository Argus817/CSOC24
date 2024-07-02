# Point Addition

## Description

While working with elliptic curve cryptography, we will need to add points together. In the background challenges, we did this geometrically by finding a line that passed through two points, finding the third intersection and then reflecting along the y-axis.  

It turns out that there is an efficient algorithm for calculating the point addition law for an elliptic curve.  

Taken from "An Introduction to Mathematical Cryptography", *Jeffrey Hoffstein, Jill Pipher, Joseph H. Silverman*, the following algorithm will calculate the addition of two points on an elliptic curve  

**Algorithm for the addition of two points: P + Q**  

(a) If $P = O$, then $P + Q = Q$.<br>(b) Otherwise, if $Q = O$, then $P + Q = P$.<br>(c) Otherwise, write $P = (x_1, y_1)$ and $Q = (x_2, y_2)$.<br>(d) If $x_1 = x_2$ and $y_1 = −y_2$, then $P + Q = O$.<br>(e) Otherwise:<br>  (e1) if $P ≠ Q: λ = \frac{(y_2 - y_1)}{(x_2 - x_1)}$<br>  (e2) if $P = Q: λ = \frac{(3{x_1}^2 + a)}{2y_1}$<br>(f) $x_3 = λ^2 − x_1 − x_2$,    $y_3 = λ(x_1 −x_3) − y_1$ <br>(g) $P + Q = (x_3, y_3)$  

> We are working with a finite field, so the above calculations should be done `mod p`, and we do not "divide" by an integer, we instead multiply by the modular inverse of a number. e.g. `1 / 5 = 9 mod 11`.  

We will work with the following elliptic curve, and prime:  

$E: Y^2 = X^3 + 497 X + 1768$, $p: 9739$  

> You can test your algorithm by asserting: `X + Y = (1024, 4440)` and `X + X = (7284, 2107)` for `X = (5274, 2841)` and `Y = (8669, 740)`.  

Using the above curve, and the points `P = (493, 5564), Q = (1539, 4742), R = (4403,5202)`, find the point `S(x,y) = P + P + Q + R` by implementing the above algorithm.  

> After calculating `S`, substitute the coordinates into the curve. Assert that the point `S` is in $E(F_p)$

## Solution

We are given an elliptical curve $E(F_p)$ and points $P$, $Q$ and $R$. The objective is to find $S$ such that $S = P+P+Q+R$ using the addition operator of elliptical curves. I implemented the given addition algorithm in the solution complete with addition and subtraction.

Complete solution is given in [`solve.py`](./solve.py).

```bash
$ python3 solve.py 
crypto{4215,2162}
```

## Answer

`crypto{4215,2162}`
