p = 28151

def isGen(g,p):
    power = 1
    for i in range(1,p-1):
        power = (power * g) % p
        if power==1:
            return False
    return True

def main():
    for i in range(2,p):
        if isGen(i,p):
            print(f"{i} is a generator")
            break
            
main()
