# Diffie-Hellman Starter 2

## Description

Every element of a finite field $F_p$ can be used to make a subgroup $H$ under repeated action of multiplication. In other words, for an element $g:\ H = \{g, g^2, g^3, ...\}$ in mod $p$.  

A primitive element of $F_p$ is an element whose subgroup $H = F_p$, *i.e.*, every element of $F_p$, can be written as $g^n\ mod\ p$ for some integer $n$. Because of this, primitive elements are sometimes called generators of the finite field.  

For the finite field with `p = 28151` find the smallest element `g` which is a primitive element of $F_p$.  

> This problem can be solved by brute-force, but there's also clever ways to speed up the calculation.

## Solution

Given `p = 28151`, we have to find the smallest element `g` such that $g\ \epsilon\ F_p$ and g is a primitive element of $F_p$. Since we have to find the smallest element that fits the conditions, bruteforcing is possible starting from `2`. We can test each element and check whether it is a primitive element or not by testing whether the consecutive powers of that element make up the non-zero elements or not.

Complete solution is given in [`solve.py`](./solve.py).

```bash
$ python3 solve.py 
7 is a generator
```

## Answer

`7`
