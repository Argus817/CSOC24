from pwn import xor

st = "label"
no = 13

flag = xor( st.encode(), b"\x0d"*len(st) ).decode()
print("crypto{"+flag+"}")
