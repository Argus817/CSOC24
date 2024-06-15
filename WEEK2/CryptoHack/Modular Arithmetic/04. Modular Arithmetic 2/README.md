# Modular Arithmetic 2

## Description

We'll pick up from the last challenge and imagine we've picked a modulus $p$, and we will restrict ourselves to the case when $p$ is prime.  

The integers modulo $p$ define a field, denoted $F_p$.  

> If the modulus is not prime, the set of integers modulo $n$ define a ring.  

A finite field $F_p$ is the set of integers `{0,1,...,p-1}`, and under both addition and multiplication there is an inverse element $b$ for every element $a$ in the set, such that $a + b = 0$ and $a * b = 1$.  

> Note that the identity element for addition and multiplication is different! This is because the identity when acted with the operator should do nothing: $a + 0 = a$ and $a * 1 = a$.  

Lets say we pick $p = 17$. Calculate $3^{17}\ mod\ 17$. Now do the same but with $5^{17}\ mod\ 17$.  

What would you expect to get for $7^{16}\ mod\ 17$? Try calculating that.  

This interesting fact is known as Fermat's little theorem. We'll be needing this (and its generalisations) when we look at RSA cryptography.  

Now take the prime $p = 65537$. Calculate $273246787654^{65536}\ mod\ 65537$.  

Did you need a calculator?

## Solution

First we are to calculate $3^{17}\ mod\ 17$ and $5^{17}\ mod\ 17$ for prime $p = 17$.

```python
$ python3
>>> pow(3,17,17)
3
>>> pow(5,17,17)
5
>>>
```

From this, we can conclude that for prime number $p$ and any $x\ \epsilon\ F_p$, $x^p \equiv x\ mod\ p$.

Next, to calculate $7^{16}\ mod\ 17$...

```python
$ python3
>>> pow(7,16,17)
1
>>>
```

Hence, we can conclude that for prime number $p$ and any $x\ \epsilon\ F_p$, $x^{p-1} \equiv 1\ mod\ p$.

So, if we have prime $p = 65537$ and we have to calculate $273246787654^{65536}\ mod\ 65537$, <br>consider<br>
$p = 65537$<br>
$x = 273246787654\ mod\ 65537, x\ \epsilon\ F_p$

Hence <br>$273246787654^{65536}\ mod\ 65537 \equiv (273246787654\ mod\ 65537)^{65536}\ mod\ 65537 \equiv x^{p-1}\ mod\ p \equiv 1$

## Answer

`1`
