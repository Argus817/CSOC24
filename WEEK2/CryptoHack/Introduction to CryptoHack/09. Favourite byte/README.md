# Favourite byte

## Description

For the next few challenges, you'll use what you've just learned to solve some more XOR puzzles.  

I've hidden some data using XOR with a single byte, but that byte is a secret. Don't forget to decode from hex first.  

`73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d`

## Solution

We are given a hex value that we can convert to bytes using `unhexlify()` function from `binascii` module. It is given that the data was XORed with a secret byte and the result is given. So to find the hidden data we would need to XOR the given data with that same byte.

We know that the value of a byte in integer ranges from 0 to 255. Hence we can try all possibilities in small amount of time and check if the flag format exists in any possibility.

Complete solution given in [`solve.py`](./solve.py).

```bash
$ python3 solve.py
b'crypto{0x10_15_my_f4v0ur173_by7e}'
```

## Answer

`crypto{0x10_15_my_f4v0ur173_by7e}`
