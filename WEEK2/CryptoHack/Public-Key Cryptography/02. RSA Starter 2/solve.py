p = 17
q = 23

N = p*q
e = 65537

PT = 12
CT = pow(PT,e,N)
print(f"CT = {CT}")
