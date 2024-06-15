# Modular Inverting

## Description

As we've seen, we can work within a finite field $F_p$, adding and multiplying elements, and always obtain another element of the field.  

For all elements $g$ in the field, there exists a unique integer $d$ such that $g × d ≡ 1\ mod\ p$.

This is the multiplicative inverse of $g$.  

**Example**: $7 × 8 = 56 ≡ 1\ mod\ 11$  

What is the inverse element: $3 × d ≡ 1\ mod\ 13$?  

> #### Hint
> 
> Think about the little theorem we just worked with. How does this help you find the inverse of an element?

## Solution

Given that $3 × d ≡ 1\ mod\ 13$, we have to find the value of $d$.

Using Fermat's Little Theorem, we know that 

$3^{13-1} \equiv 1 \ mod\ 13$<br>
$\therefore 3^{12}\equiv1\ mod\ 13$<br>
$\therefore3×3^{11}\equiv1\ mod\ 13$<br>
$\therefore3×(3^{11}\ mod\ 13) \equiv1\ mod\ 13$

$\therefore$ we can write $d = 3^{11}\ mod\ 13 = 9$

```python
$ python3
>>> pow(3,11,13)
9
>>>
```



## Answer

`9`
