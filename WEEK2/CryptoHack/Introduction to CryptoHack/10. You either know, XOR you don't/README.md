# You either know, XOR you don't

## Description

I've encrypted the flag with my secret key, you'll never be able to guess it.  

> #### Hint
> 
> Remember the flag format and how it might help you in this challenge!  

`0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104`

## Solution

We are given a hex string which is to be converted into bytes using `unhexlify()`. The flag was encrypted using a secret key and the result is given to us. This means an arbitrary flag of the format `crypto{...}` was XORed with a secret key. Hence if we XOR the given data with `crypto{ + rest bytes equal to zero`, we may get the first 7 characters of the secret key.

I implemented the above solution in [`search.py`](./search.py).

```bash
$ python3 search.py
b"myXORkeH\x0b&!\x7f'4.\x17]\x0e\x07\n<[\x10>%&!\x7f'4.\x17]\x0e\x07~&4Q\x15\x01\x04"
```

We now have the first 7 characters of the secret key to be `myXORke`. It is only logical that the next character be `y`. The secret key could be the sequence `myXORkey` repeatedly, which worked.

Complete solution given in [`solve.py`](./solve.py).

```bash
$ python3 solve.py
b'crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}'
```

## Answer

`crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}`
