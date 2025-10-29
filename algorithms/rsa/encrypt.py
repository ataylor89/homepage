def encrypt(msg, key):
    ciphertext = ""
    codes = msg.encode("utf-8")
    keylen = len(key)
    for i in range(0, len(codes)):
        (n, e, d) = key[i % keylen]
        size = util.size(n)
        cipher = util.power_mod_n(codes[i], e, n)
        encoding = util.encode(cipher, size)
        ciphertext += encoding
    return ciphertext

if __name__ == "__main__":
    import parser, util, argparse
    argparser = argparse.ArgumentParser(prog="encrypt.py", description="Encrypt a message")
    argparser.add_argument("-m", "--msgfile", type=str, required=True)
    argparser.add_argument("-k", "--keyfile", type=str, default="key.txt")
    argparser.add_argument("-o", "--output", type=str)
    args = argparser.parse_args()
    with open(args.msgfile, "r") as msgfile:
        msg = msgfile.read()
    key = parser.parse_key(args.keyfile)
    ciphertext = encrypt(msg, key)
    if args.output:
        with open(args.output, "w") as outputfile:
            outputfile.write(ciphertext)
    else:
        print(ciphertext, end="")
else:
    from algorithms.rsa import parser, util
