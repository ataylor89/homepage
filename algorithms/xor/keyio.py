from algorithms.xor import util

def load(path):
    with open(path, "r") as file:
        contents = file.read()
        key = util.decode(contents)
        return key

def save(key, path):
    with open(path, "w") as file:
        encoding = util.encode(key)
        file.write(encoding)
