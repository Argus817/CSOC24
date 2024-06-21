from binascii import unhexlify
with open('output.txt', 'r') as f:
    s = f.read()

e = ""

for i in range(0,len(s),4):
    e += format(int(s[i:i+2],16)^int(s[i:i+4],16), '02x')

print(unhexlify(e.encode()))
