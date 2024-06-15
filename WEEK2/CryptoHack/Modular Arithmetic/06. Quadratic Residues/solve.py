p = 29
ints = [14,6,11]

for i in range(p):
    sq = pow(i,2,p)
    if sq in ints:
        print(f"Num = {i}, square = {sq}")
