## challenge_2

#### Attachments: [`encoded.txt`](./encoded.txt)

## Solution

We are given only a single file [`encoded.txt`](./encoded.txt) which looks like the following...

```
01000011 01010011 01001111 01000011 00110010 33 7b 6a 75 35 37 5f ZDFmZjNyM243XzNuYw== 60 144 61 156 66 65 137 154 60 154 175
```

At first glimpse, it looks like it contains data in different encoding schemes. The first five data values are in binary. Converting them to characters gave the start of the flag...

```
01000011 >> 'C'
01010011 >> 'S'
01001111 >> 'O'
01000011 >> 'C'
00110010 >> '2'
```

The next 7 data values are hexadecimal values and converting them to characters gave the following...

```
33 >> '3'
7b >> '{'
6a >> 'j'
75 >> 'u'
35 >> '5'
37 >> '7'
5f >> '_'
```

The next data value is a base64 encoded string which on decoding produced the next part of the flag.

```bash
$ echo ZDFmZjNyM243XzNuYw== | base64 -d
d1ff3r3n7_3nc
```

The last part containing the numbers `['60', '144', '61', '156', '66', '65', '137', '154', '60', '154', '175']` proved to be tricky. On directly converting them to characters, some unprintable characters were also found. So these are not ASCII values. The last value `175` should correspond to the character `}` to complete the flag format. I tried using XOR. I found that on XORing `175` with `210` I obtained `125` which was the ASCII value of `}`. But XORing the other values with `210` resulted in unprintable characters.

The answer turned out to be in bases. I noticed each digit was less than 8, so I concluded that the numbers must be in base 8. Converting from base 8 to characters resulted in the following...

```
60  >> '0'
144 >> 'd'
61  >> '1'
156 >> 'n'
66  >> '6'
65  >> '5'
137 >> '_'
154 >> 'l'
60  >> '0'
154 >> 'l'
175 >> '}'
```

Complete solution given in [`solve.py`](/solve.py).

```bash
$ python3 solve.py
CSOC23{ju57_d1ff3r3n7_3nc0d1n65_l0l}
```

## Flag

`CSOC23{ju57_d1ff3r3n7_3nc0d1n65_l0l}`
