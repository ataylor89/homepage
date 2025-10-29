import sys

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

def main():
    if len(sys.argv) != 2:
        print("Usage: python rot13.py <msgfile>")
        sys.exit(0)
    file = open(sys.argv[1], "r")
    message = file.read()
    result = rot13(message)
    print(result, end="")

if __name__ == "__main__":
    main()
