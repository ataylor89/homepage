table = {}

for i in range(0, 26):
    table[chr(ord("a") + i)] = chr(ord("a") + (i + 13) % 26)
    table[chr(ord("A") + i)] = chr(ord("A") + (i + 13) % 26)

def rot13(message):
    result = ""
    for letter in message:
        substitution = table[letter] if letter in table else letter
        result += substitution
    return result

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(prog="rot13.py", description="Encrypt or decrypt a message using rot13")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("message", type=str, nargs="?")
    group.add_argument("-m", "--msgfile", type=str)
    parser.add_argument("-o", "--output", type=str)
    args = parser.parse_args()
    if args.msgfile:
        with open(args.msgfile, "r") as msgfile:
            message = msgfile.read()
    else:
        message = args.message
    output = rot13(message)
    if args.output:
        with open(args.output, "w") as outputfile:
            outputfile.write(output)
    else:
        print(output, end="")
