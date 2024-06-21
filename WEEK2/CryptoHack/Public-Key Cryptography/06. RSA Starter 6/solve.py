from hashlib import sha256

def read_key_file(filename):
    values = {}
    with open(filename, 'r') as file:
        for line in file:
            key, value = line.split('=')
            values[key.strip()] = int(value.strip())
    return values

N,d = tuple(read_key_file("private.key").values())
flag = b"crypto{Immut4ble_m3ssag1ng}"

hashed = sha256(flag).hexdigest()
signature = pow(int(hashed,base=16),d,N)
print(f"signature = {signature}")
