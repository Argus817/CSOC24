from base64 import b64decode
with open('encoded.txt','r') as f:
    data = f.read().split(' ')

flag = ""
binary = [chr(int(i,base=2)) for i in data[0:5]]
hexa = [chr(int(i,base=16)) for i in data[5:12]]
b64 = b64decode(data[12])
flag += "".join(binary)+"".join(hexa)+b64.decode()

base8 = [chr(int(i,base=8)) for i in data[13:]]
flag += "".join(base8)

print(flag)
