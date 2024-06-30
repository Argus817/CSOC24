p = 28151

def isGen(g,p):
    H = set()
    power = 1
    for i in range(1,p):
        power = (power * g) % p
        if power in H:
            return False
        H.add(power)
    return True

def main():
    for i in range(2,p):
        if isGen(i,p):
            print(f"{i} is a generator")
            break
            
main()
