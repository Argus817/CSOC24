# Modular Binomials

## Description

Rearrange the following equations to get the primes `p,q`  

```
N = p*q  
c1 = (2*p + 3*q)**e1 mod N  
c2 = (5*p + 7*q)**e2 mod N  
```

**Challenge files:**  

- [data.txt](./data.txt)

#### Attachments: [`data.txt`](./data.txt)

## Solution

We are given the the values `N`, `e1`, `e2`, `c1`, `c2` and the relations $N = pq$, $c_1 = (2p+3q)^{e_1}\ mod\ N$ and $c_2 = (5p+7q)^{e_2}\ mod\ N$.

Consider ${c_1}^{e_2}\equiv (2p+3q)^{e_1 e_2}\ mod\ N$, ${c_2}^{e_1}\equiv (5p+7q)^{e_1 e_2}\ mod\ N$<br>$2^{-e_1e_2}{c_1}^{e_2}\equiv2^{-e_1e_2}(2p)^{e_1e_2}+2^{-e_1e_2}(3q)^{e_1e_2}\ mod\ N \equiv p^{e_1e_2}+2^{-e_1e_2}(3q)^{e_1e_2}\ mod\ N$<br>$5^{-e_1e_2}{c_2}^{e_1}\equiv 5^{-e_1e_2}(5p)^{e_1e_2}+5^{-e_1e_2}(7q)^{e_1e_2}\ mod\ N\equiv p^{e_1e_2}+5^{-e_1e_2}(7q)^{e_1e_2}\ mod\ N$

Hence, $5^{-e_1e_2}{c_2}^{e_1} - 2^{-e_1e_2}{c_1}^{e_2}\equiv 5^{-e_1e_2}(7q)^{e_1e_2} - 2^{-e_1e_2}(3q)^{e_1e_2}\ mod\ N$<br>and gcd($5^{-e_1e_2}{c_2}^{e_1} - 2^{-e_1e_2}{c_1}^{e_2}\ mod\ N$,  $N$)$\ = q$

Complete solution is given in [`solve.py`](./solve.py).

```bash
$ python3 solve.py
crypto{112274000169258486390262064441991200608556376127408952701514962644340921899196091557519382763356534106376906489445103255177593594898966250176773605432765983897105047795619470659157057093771407309168345670541418772427807148039207489900810013783673957984006269120652134007689272484517805398390277308001719431273,132760587806365301971479157072031448380135765794466787456948786731168095877956875295282661565488242190731593282663694728914945967253173047324353981530949360031535707374701705328450856944598803228299967009004598984671293494375599408764139743217465012770376728876547958852025425539298410751132782632817947101601}
```

## Answer

`crypto{112274000169258486390262064441991200608556376127408952701514962644340921899196091557519382763356534106376906489445103255177593594898966250176773605432765983897105047795619470659157057093771407309168345670541418772427807148039207489900810013783673957984006269120652134007689272484517805398390277308001719431273,132760587806365301971479157072031448380135765794466787456948786731168095877956875295282661565488242190731593282663694728914945967253173047324353981530949360031535707374701705328450856944598803228299967009004598984671293494375599408764139743217465012770376728876547958852025425539298410751132782632817947101601}`