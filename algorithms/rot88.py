import sys

def rot88(message):
    result = ""
    for character in message:
        code = ord(character)
        code = (code + 0x88000) % 0x110000
        result += chr(code)
    return result

def main():
    if len(sys.argv) != 2:
        print("Usage: python rot88.py <msgfile>")
        sys.exit(0)
    file = open(sys.argv[1], "r")
    message = file.read()
    result = rot88(message)
    print(result, end="")

if __name__ == "__main__":
    main()
