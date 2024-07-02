# Point Negation

## Description

In the background section, we covered the basics of how we can view point addition over an elliptic curve as being an abelian group operation. In this geometric picture we allowed the coordinates on the curve to be any real number.  

To apply elliptic curves in a cryptographic setting, we study elliptic curves which have coordinates in a finite field $F_p$.  

We will still be considering elliptic curves of the form $E: Y^2 = X^3 + a X + b$ , which satisfy the following conditions: $a,b\ ∈\ F_p$ and $4a^3 + 27 b^2 ≠ 0$. However, we no longer think of the elliptic curve as a geometric object, but rather a set of points defined by  

> $E(F_p) = \{(x,y) : x,y ∈ F_p$ satisfying: $y^2 = x^3 + a x + b\} ∪ O$

Note: Everything we covered in the background still holds. The identity of the group is the point at infinity: O, and the addition law is unchanged. Given two points in $E(F_p)$, the addition law will generate another point in $E(F_p)$.  

For all the challenges in the starter set, we will be working with the elliptic curve  

$E: Y^2 = X^3 + 497 X + 1768,\ p: 9739$

Using the above curve, and the point `P(8045,6936)`, find the point `Q(x,y)` such that `P + Q = O`.  

Remember, we're working in a finite field now, so you'll need to work correctly with negative numbers.  

**Resources:**  
  - [The Animated Elliptic Curve: Visualizing Elliptic Curve Cryptography](https://curves.xargs.org/)

## Solution

Given elliptic curve $E: Y^2 = X^3 + 497 X + 1768$ in field $F_p$ where prime $p = 9739$ and point $P(8045,6936)$. We have to find $Q$ such that $P + Q = O$. 

Since $O$ lies on all vertical lines at infinity, $Q$ must lie on the vertical line (slope $= \infty$) passing through $P(8045,6936)$. This line is $X = 8045$. Since the elliptic curve is symmetric on the $X$-axis, this means that the point $Q$ should be $Q(8045,-6936)$. But we are working in $F_{9739}$, hence $Q$ should be $Q(8045,-6936)\equiv Q(8045,2803)\ mod\ 9739$.

## Answer

`crypto{8045,2803}`
