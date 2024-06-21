# Factoring

## Description

So far we've been using the product of small primes for the modulus, but small primes aren't much good for RSA as they can be factorised using [modern](https://en.wikipedia.org/wiki/Lenstra_elliptic-curve_factorization) [methods](https://en.wikipedia.org/wiki/General_number_field_sieve).  

What is a "small prime"? There was an [RSA Factoring Challenge](https://en.wikipedia.org/wiki/RSA_Factoring_Challenge) with cash prizes given to teams who could factorise RSA moduli. This gave insight to the public into how long various key sizes would remain safe. Computers get faster, algorithms get better, so in cryptography it's always prudent to err on the side of caution.  

These days, using primes that are at least 1024 bits long is recommended—multiplying two such 1024 primes gives you a modulus that is 2048 bits large. RSA with a 2048-bit modulus is called RSA-2048.  

Some say that to really remain future-proof you should use RSA-4096 or even RSA-8192. However, there is a tradeoff here; it takes longer to generate large prime numbers, plus modular exponentiations are predictably slower with a large modulus.  

Factorise the 150-bit number `510143758735509025530880200653196460532653147` into its two constituent primes. Give the smaller one as your answer.  

**Resources:**  

- [How big an RSA key is considered secure today?](https://crypto.stackexchange.com/questions/1978/how-big-an-rsa-key-is-considered-secure-today/1982#1982)  
- [primefac-fork](https://github.com/elliptic-shiho/primefac-fork)

## Solution

Given a 150-bit number, we have to factorise it into constituent primes. Factorisation of large numbers is a computationally intensive task but there exist algorithms to factorise small enough numbers in minimum possible time. Also, [FactorDB](factordb.com) is a database that stores many large numbers and their factorisations. 

I used the built-in function in SageMath to factorise the given number.

```bash
$ sage
sage: factor(510143758735509025530880200653196460532653147)
19704762736204164635843 * 25889363174021185185929
```

## Answer

`19704762736204164635843`
