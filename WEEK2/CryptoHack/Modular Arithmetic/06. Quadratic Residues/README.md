# Quadratic Residues

## Description

We've looked at multiplication and division in modular arithmetic, but what does it mean to take the square root modulo an integer?  

For the following discussion, let's work modulo $p = 29$. We can take the integer $a = 11$ and calculate $a^2 = 5\ mod\ 29$.  

As $a = 11,\ a^2 = 5$, we say the square root of $5$ is $11$.  

This feels good, but now let's think about the square root of $18$. From the above, we know we need to find some integer $a$ such that $a^2 = 18$  

Your first idea might be to start with $a = 1$ and loop to $a = p-1$. In this discussion $p$ isn't too large and we can quickly look.  

Have a go, try coding this and see what you find. If you've coded it right, you'll find that for all $a\ \epsilon\ F_p^*$ you never find an $a$ such that $a^2 = 18$. 

What we are seeing, is that for the elements of $F_p^*$, not every element has a square root. In fact, what we find is that for roughly one half of the elements of $F_p^*$, there is no square root.  

> We say that an integer $x$ is a *Quadratic Residue* if there exists an $a$ such that $a^2 = x\ mod\ p$. If there is no such solution, then the integer is a *Quadratic Non-Residue*.  

In other words, $x$ is a quadratic residue when it is possible to take the square root of $x$ modulo an integer $p$.  

In the below list there are two non-quadratic residues and one quadratic residue.  

Find the quadratic residue and then calculate its square root. Of the two possible roots, submit the smaller one as the flag.  

> If $a^2 = x $ then $(-a)^2 = x$. So if $x$ is a quadratic residue in some finite field, then there are always two solutions for $a$.  

```
p = 29  
ints = [14, 6, 11]
```

## Solution

We are given a prime number $p = 29$ and 3 integers `[14, 6, 11]` out of which only one is a quadratic residue. This means that there exists at least a number $x$ from 0 to $p-1$ such that $x^2\ mod\ p$ matches only one integer in the list. Hence I iterated from $0$ to $p-1$ and found the square mod p and checked if the square was present in the list.

Complete solution is present in [`solve.py`](./solve.py).

```bash
$ python3 solve.py
Num = 8, square = 6
Num = 21, square = 6
```

## Answer

`8`
