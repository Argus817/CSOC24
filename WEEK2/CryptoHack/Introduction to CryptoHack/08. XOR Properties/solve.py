from pwn import xor
from binascii import unhexlify

KEY1 = unhexlify(b"a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
K2xK1 = unhexlify(b"37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
K2xK3 = unhexlify(b"c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1") 
FLAGxK1xK3xK2 = unhexlify(b"04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

FLAG = xor( FLAGxK1xK3xK2, xor( KEY1, K2xK3 ) )

print(FLAG)
