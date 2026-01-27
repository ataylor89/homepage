def encode(key):
    encoding = [chr(x) for x in key]
    return "".join(encoding)

def decode(str):
    decoding = list(map(lambda x: ord(x), str))
    return decoding
