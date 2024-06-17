a = 288260533169915
p = 1007621497415251

data = list(map(int,open("output.txt",'r').read().strip()[1:-1].replace(' ','').split(',')))

leg = lambda x,prime : pow(x,(prime-1)//2,prime)

assert leg(a,p)==1

binary = ""
for num in data:
    if leg(num,p)==1:
        binary += '1'
    else:
        binary += '0'

flag = ""
for i in range(0,len(binary),8):
    flag += chr(int(binary[i:i+8], base=2))

print(flag)
