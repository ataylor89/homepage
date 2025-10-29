import random
import argparse

def gen_key(keylen):
    key = [chr(random.randint(0, 255)) for i in range(0, keylen)]
    return "".join(key)

def main():
    parser = argparse.ArgumentParser(prog="keygen.py", description="Create an XOR key", epilog="Thanks for reading")
    parser.add_argument("-kl", "--keylength", type=int, default=1024)
    parser.add_argument("-o", "--output", type=str, default="key.txt")
    args = parser.parse_args()
    keylen = args.keylength
    filepath = args.output
    key = gen_key(keylen)
    with open(filepath, "w") as file:
        file.write(key)

if __name__ == "__main__":
    main()
