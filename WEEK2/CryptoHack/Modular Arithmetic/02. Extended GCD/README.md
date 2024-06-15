# Extended GCD

## Description

Let `a` and `b` be positive integers.  

The extended Euclidean algorithm is an efficient way to find integers `u,v` such that  

`a * u + b * v = gcd(a,b)`  

> Later, when we learn to decrypt RSA, we will need this algorithm to calculate the modular inverse of the public exponent.  

Using the two primes `p = 26513, q = 32321`, find the integers `u,v` such that  

`p * u + q * v = gcd(p,q)`  

Enter whichever of `u` and `v` is the lower number as the flag.  

> Knowing that `p,q` are prime, what would you expect `gcd(p,q)` to be? For more details on the extended Euclidean algorithm, check out [this page](https://web.archive.org/web/20230511143526/http://www-math.ucdenver.edu/~wcherowi/courses/m5410/exeucalg.html).

## Solution

I simply implemented the Extended Eucledean Algorithm in [`solve.py`](./solve.py).

## Answer

`-8404`
