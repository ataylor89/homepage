def crypt(msg, key):
    msglen = len(msg)
    keylen = len(key)
    codepoints = list(map(lambda x: ord(x), msg))
    result = [chr(codepoints[i] ^ key[i % keylen]) for i in range(msglen)]
    return ''.join(result)
