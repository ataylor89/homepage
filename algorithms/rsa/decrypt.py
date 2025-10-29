def decrypt(ciphertext, key):
    message = ""
    keylen = len(key)
    start = 0
    end = 0
    i = 0
    while start < len(ciphertext):
        (n, e, d) = key[i % keylen]
        size = util.size(n)
        end = start + size
        substr = ciphertext[start:end]
        cipher = util.decode(substr)
        message += chr(util.power_mod_n(cipher, d, n))
        i += 1
        start += size
    return message

if __name__ == "__main__":
    import parser, util, argparse
    argparser = argparse.ArgumentParser(prog="decrypt.py", description="Decrypt a message")
    argparser.add_argument("-c", "--cipherfile", type=str, required=True)
    argparser.add_argument("-k", "--keyfile", type=str, default="key.txt")
    argparser.add_argument("-o", "--output", type=str)
    args = argparser.parse_args()
    with open(args.cipherfile, "rb") as cipherfile:
        ciphertext = cipherfile.read()
    ciphertext = ciphertext.decode("utf-8")
    key = parser.parse_key(args.keyfile)
    msg = decrypt(ciphertext, key)
    if args.output:
        with open(args.output, "w") as outputfile:
            outputfile.write(msg)
    else:
        print(msg, end="")
else:
    from algorithms.rsa import parser, util
