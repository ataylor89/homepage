def load(path):
    key = []
    with open(path, "r") as file:
        for line in file:
            tokens = line.split()
            n, e, d = int(tokens[0][2:]), int(tokens[1][2:]), int(tokens[2][2:])
            key.append((n, e, d))
    return key

def save(key, path):
    with open(path, "w") as file:
        for (n, e, d) in key:
            file.write("n=%d e=%d d=%d" %(n, e, d))
