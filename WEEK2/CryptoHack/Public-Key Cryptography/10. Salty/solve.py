from Crypto.Util.number import long_to_bytes

def read_key_file(filename):
    values = {}
    with open(filename, 'r') as file:
        for line in file:
            key, value = line.split('=')
            values[key.strip()] = int(value.strip())
    return values
n,e,ct = tuple(read_key_file("output.txt").values())

print(long_to_bytes(ct))
