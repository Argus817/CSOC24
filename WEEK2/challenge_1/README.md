# challenge_1

#### Attachments: [`source.enc`](./source.enc) and [`output.txt`](./output.txt)

## Solution

We are given two files. [`output.txt`](./output.txt) contains some string in hex (below)...

```
43104f0c32017b48340179266203350636025f6b6e0a5f2730423f42
```

While, [`source.enc`](./source.enc) contains some data in base64 (below)...

```
d2l0aCBvcGVuKCdmbGFnLnR4dCcsICdyJykgYXMgZjoKICAgIGZsYWcgPSBmLnJlYWQoKQoKcyA9ICcnLmpvaW4oZm9ybWF0KG9yZChpKSwgJzAyeCcpIGZvciBpIGluIGZsYWcpCmUgPSAiIgoKZm9yIGkgaW4gcmFuZ2UoMCxsZW4ocyksNCk6CiAgICBlICs9IGZvcm1hdChpbnQoc1tpOmkrMl0sMTYpXmludChzW2k6aSs0XSwxNiksICcwMngnKQoKd2l0aCBvcGVuKCdvdXRwdXQudHh0JywgJ3cnKSBhcyBmOgogICAgZi53cml0ZShlKQ==
```

Decoding from base64, the data turned out to be a python code. On analysing it, I figured out the text in [`output.txt`](./output.txt) was generated from this code.

```
$ cat source.enc | base64 -d
with open('flag.txt', 'r') as f:
    flag = f.read()

s = ''.join(format(ord(i), '02x') for i in flag)
e = ""

for i in range(0,len(s),4):
    e += format(int(s[i:i+2],16)^int(s[i:i+4],16), '02x')

with open('output.txt', 'w') as f:
    f.write(e)

$ cat source.enc | base64 -d > source.py
```

On further analysing the code, I figured out that it iterated over 2 consecutive bytes. In each iteration, it took the first byte as a whole and both the bytes together as a whole and XORed them together. According to the properties of XOR, doing the same thing again would result in the flag. I manipulated [`source.py`](./source.py) and wrote the solution in [`solve.py`](./solve.py).

```bash
$ python3 solve.py
b'CSOC23{345y_ba5364_4nd_x0r?}'
```

## Flag

`CSOC23{345y_ba5364_4nd_x0r?}`


