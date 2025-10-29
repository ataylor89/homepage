def parse_key(path):
    key = []
    file = open(path, "r")
    for line in file:
        tokens = line.split()
        n, e, d = int(tokens[0][2:]), int(tokens[1][2:]), int(tokens[2][2:])
        key.append((n, e, d))
    return key
