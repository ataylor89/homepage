def crypt(msg, key):
    msglen = len(msg)
    keylen = len(key)
    msgcodes = list(map(lambda x: ord(x), msg))
    output = [chr(msgcodes[i] ^ key[i % keylen]) for i in range(0, msglen)]
    return ''.join(output)
