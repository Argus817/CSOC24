from binascii import unhexlify
from pwn import xor

data = unhexlify(b"0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
print( xor( data , b"crypto{"+b"\x00"*(len(data)-len(b"crypto{")) ))
