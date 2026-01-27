def rot88(message):
    result = ''
    for character in message:
        code = ord(character)
        code = (code + 0x88000) % 0x110000
        result += chr(code)
    return result
