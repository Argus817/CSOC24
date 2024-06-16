# Chinese Remainder Theorem

## Description

The Chinese Remainder Theorem gives a unique solution to a set of linear congruences if their moduli are coprime.  

This means, that given a set of arbitrary integers `a[i]`, and pairwise coprime integers `n[i]`, such that the following linear congruences hold:  

> Note "pairwise coprime integers" means that if we have a set of integers `{n1, n2, ..., n[i]}`, all pairs of integers selected from the set are coprime: `gcd(n[i], n[j]) = 1`.  

```
x ≡ a1 mod n1  
x ≡ a2 mod n2  
...  
x ≡ a[n] mod n[n]  
```

There is a unique solution `x ≡ a mod N` where `N = n1 * n2 * ... * n[n]`.  

In cryptography, we commonly use the Chinese Remainder Theorem to help us reduce a problem of very large integers into a set of several, easier problems.  

Given the following set of linear congruences:  

```
x ≡ 2 mod 5  
x ≡ 3 mod 11  
x ≡ 5 mod 17  
```

Find the integer `a` such that `x ≡ a mod 935`  

> Starting with the congruence with the largest modulus, use that for `x ≡ a mod p` we can write `x = a + k*p` for arbitrary integer `k`.

## Solution

We are given 3 congruences for moduli $5,11,17$ and we are to find the congruence when modulus is $5×11×17=935$. We utilise Chinese Remainder Theorem to find it.

Given

$x\equiv 2\ mod\ 5$<br>$x\equiv 3\ mod\ 11$<br>$x\equiv 5\ mod\ 17$<br>We have to find $a$ such that $x\equiv a\ mod\ 935$

Let $t_1 = 2×(11×17)×[(11×17)^{-1}\ mod\ 5] = 2×11×17×3 = 1122$<br>Let $t_2 = 3×(5×17)×[(5×17)^{-1}\ mod\ 11 ] = 3×5×17×7 = 1785$<br>Let $t_3 = 5×(5×11)×[(5×11)^{-1}\ mod\ 17] = 5×5×11×13 = 3575$

$\therefore a = (t_1+t_2+t_3)\ mod\ 935 = [(1122\ mod\ 935)+(1785\ mod\ 935)+(3575\ mod\ 935)]\ mod\ 935$<br>$\therefore a = (187+850+770)\ mod\ 935 = 872\ mod\ 935$

This can be verified by SageMath's `crt()` function.

```bash
$ sage
sage: crt([2,3,5],[5,11,17])
872
```

## Answer

`872`
