def rot88(message):
    result = ""
    for character in message:
        code = ord(character)
        code = (code + 0x88000) % 0x110000
        result += chr(code)
    return result

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(prog="rot88.py", description="Encrypt or decrypt a message using rot88")
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
    output = rot88(message)
    if args.output:
        with open(args.output, "w") as outputfile:
            outputfile.write(output)
    else:
        print(output, end="")
