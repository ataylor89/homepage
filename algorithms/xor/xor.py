def crypt(msg, key):
    msglen = len(msg)
    keylen = len(key)
    msgcodes = list(map(lambda x: ord(x), msg))
    keycodes = list(map(lambda x: ord(x), key))
    out = [chr(msgcodes[i] ^ keycodes[i % keylen]) for i in range(0, msglen)]
    return "".join(out)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(prog="xor.py", description="Encrypt or decrypt a message")
    parser.add_argument("-m", "--msgfile", type=str, required=True)
    parser.add_argument("-k", "--keyfile", type=str, default="key.txt")
    parser.add_argument("-o", "--output", type=str)
    args = parser.parse_args()
    with open(args.msgfile, "r") as msgfile:
        msg = msgfile.read()
    with open(args.keyfile, "r") as keyfile:
        key = keyfile.read()
    output = crypt(msg, key)
    if args.output:
        with open(args.output, "w") as outputfile:
            outputfile.write(output)
    else:
        print(output, end="")
