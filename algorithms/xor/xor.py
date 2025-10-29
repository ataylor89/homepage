import sys

def crypt(msg, key):
    msglen = len(msg)
    keylen = len(key)
    msgcodes = list(map(lambda x: ord(x), msg))
    keycodes = list(map(lambda x: ord(x), key))
    out = [chr(msgcodes[i] ^ keycodes[i % keylen]) for i in range(0, msglen)]
    return "".join(out)

def main():
    if len(sys.argv) != 2:
        print("Usage: python xor.py <msgfile>")
        sys.exit(0)
    msgfile = open(sys.argv[1], "r")
    msg = msgfile.read()
    keyfile = open("key.txt", "r")
    key = keyfile.read()
    print(crypt(msg, key), end="")
    
if __name__ == "__main__":
    main()
