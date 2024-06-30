# Diffie-Hellman Starter 1

## Description

The set of integers modulo `n`, together with the operations of both addition and multiplication is a ring. This means that adding or multiplying any two elements in the set returns another element in the set.  

When the modulus is prime: `n = p`, we are guaranteed an inverse of every element in the set, and so the ring is promoted to a field. We refer to this field as a finite field $F_p$.  

The Diffie-Hellman protocol works with elements of some finite field $F_p$, where the prime modulus is typically a large prime.  

Given the prime `p = 991`, and the element `g = 209`, find the inverse element `d` such that `g * d mod 991 = 1`.

## Solution

Given `p = 991` which is prime and `g = 209`. The inverse of `g` can be easily found by extension of Fermat's Little Theorem such that the inverse $d = g^{p-2}\ mod\ p$. 

It can also be found by Python's implementation of `pow` function with 3 parameters, the exponent being `-1`.

```python
$ python3
>>> pow(209,-1,991)
569
>>> pow(209,991-2,991)
569
```

## Answer

`569`
