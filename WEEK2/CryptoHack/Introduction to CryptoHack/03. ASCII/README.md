# ASCII

## Description

ASCII is a 7-bit encoding standard which allows the representation of text using the integers 0-127.  

Using the below integer array, convert the numbers to their corresponding ASCII characters to obtain a flag.  

`[99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]`  

> #### Hint
> 
> In Python, the `chr()` function can be used to convert an ASCII ordinal number to a character (the `ord()` function does the opposite).

## Solution

We are given a list of numbers which are the ASCII representation of each character of the flag. We simply need to convert them to characters using the `chr()` function and join them together to form a string. 

Complete solution given in [`solve.py`](./solve.py).

```bash
$ python3 solve.py            
crypto{ASCII_pr1nt4bl3}
```

## Answer

`crypto{ASCII_pr1nt4bl3}`
