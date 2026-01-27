from algorithms.rsa import util

def encrypt(msg, key):
    ciphertext = ''
    codes = list(map(lambda x: ord(x), msg))
    keylen = len(key)
    for i in range(0, len(codes)):
        (n, e, d) = key[i % keylen]
        size = util.size(n)
        cipher = util.power_mod_n(codes[i], e, n)
        encoding = util.encode(cipher, size)
        ciphertext += encoding
    return ciphertext
