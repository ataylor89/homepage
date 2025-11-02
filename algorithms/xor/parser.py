from algorithms.xor import util

def parse_key(path):
    with open(path, "r") as file:
        contents = file.read()
        key = util.decode(contents)
        return key
