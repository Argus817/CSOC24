# Legendre Symbol

## Description

In Quadratic Residues we learnt what it means to take the square root modulo an integer. We also saw that taking a root isn't always possible.  

In the previous case when $p = 29$, even the simplest method of calculating the square root was fast enough, but as $p$ gets larger, this method becomes wildly unreasonable.  

Lucky for us, we have a way to check whether an integer is a quadratic residue with a single calculation thanks to Legendre. In the following, we will assume we are working modulo a prime $p$.  

Before looking at Legendre's symbol, let's take a brief detour to see an interesting property of quadratic (non-)residues.  

```
Quadratic Residue * Quadratic Residue = Quadratic Residue  
Quadratic Residue * Quadratic Non-residue = Quadratic Non-residue  
Quadratic Non-residue * Quadratic Non-residue = Quadratic Residue  
```

> Want an easy way to remember this? Replace "Quadratic Residue" with $+1$ and "Quadratic Non-residue" with $-1$, all three results are the same!  

So what's the trick? The [Legendre Symbol](https://en.wikipedia.org/wiki/Legendre_symbol) gives an efficient way to determine whether an integer is a quadratic residue modulo an odd prime $p$.  

Legendre's Symbol: $(a\  /\  p) ≡ a^{(p-1)/2}\ mod\ p$ obeys:  

```
(a / p) = 1 if a is a quadratic residue and a ≢ 0 mod p  
(a / p) = -1 if a is a quadratic non-residue mod p  
(a / p) = 0 if a ≡ 0 mod p  
```

Which means given any integer $a$, calculating `pow(a,(p-1)//2,p)` is enough to determine if $a$ is a quadratic residue.  

Now for the flag. Given the following 1024 bit prime and 10 integers, find the quadratic residue and then calculate its square root; the square root is your flag. Of the two possible roots, submit the larger one as your answer.  

> So Legendre's symbol tells us which integer is a quadratic residue, but how do we find the square root?! The prime supplied obeys $p = 3\ mod\ 4$, which allows us easily compute the square root. The answer is online, but you can figure it out yourself if you think about Fermat's little theorem.  

**Challenge files:** 

- [output.txt](./output.txt)

#### Attachments: [`output.txt`](./output.txt)

## Solution

We are given a prime `p` and a list of integers `ints` from which, one is a quadratic residue modulo `p`. We can iterate through the list `ints` and use the Legendre Symbol to check if it is a quadratic residue. 

Consider $y\ \epsilon$ `ints` and $y$ is a quadratic residue confirmed by the Legendre Symbol, we have to calculate the square root of $y$. From Fermat's Little Theorem, we have 

$y^{p-1}\equiv1\ mod\ p$<br>$\therefore$ Let $x^4 \equiv y^{p+1}\equiv y^2y^{p-1}\ mod\ p\equiv y^2\ mod\ p$<br>$\therefore y^2-x^4 \equiv 0\ mod\ p$<br>$\therefore (y-x^2)(y+x^2)\equiv0\ mod\ p$<br>$\therefore y\equiv ±x^2\ mod\ p$ or $±y\equiv x^2\ mod\ p$

Hence the modular square roots of $y$ are $x=±y^{(p+1)/4}\ mod\ p$.

> **Note:** This only works if the prime $p \equiv 3\ mod\ 4$ because only then $p+1$ is divisible by 4. 

Complete solution is given in [`solve.py`](./solve.py).

```bash
$ python3 solve.py 
85256449776780591202928235662805033201684571648990042997557084658000067050672130152734911919581661523957075992761662315262685030115255938352540032297113615687815976039390537716707854569980516690246592112936796917504034711418465442893323439490171095447109457355598873230115172636184525449905022174536414781771 is quadratic residue
Square Roots are 
93291799125366706806545638475797430512104976066103610269938025709952247020061090804870186195285998727680200979853848718589126765742550855954805290253592144209552123062161458584575060939481368210688629862036958857604707468372384278049741369153506182660264876115428251983455344219194133033177700490981696141526
and
8232236049173183678862937195287831276653989122956554214447665091513920336605945873062812694439477854741537808646890019914007590415646391519044983311757105364315128218092106114364707761008033750078377854376973994234230173507772985887244585728151706837318609420099361595002284179979838777363970347561613017613
```

## Answer

`93291799125366706806545638475797430512104976066103610269938025709952247020061090804870186195285998727680200979853848718589126765742550855954805290253592144209552123062161458584575060939481368210688629862036958857604707468372384278049741369153506182660264876115428251983455344219194133033177700490981696141526`
