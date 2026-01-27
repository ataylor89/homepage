from algorithms.exceptions import InvalidKeyError

def parse_key(path):
    key = []
    with open(path, 'r') as file:
        for index, line in enumerate(file):
            linenum = index + 1
            try:
                tokens = line.split('=')
                byte_value = int(tokens[1])
                if byte_value < 0 or byte_value > 255:
                    raise InvalidKeyError(f'Value does not fall within the range [0, 255] in line {linenum} of key file')
                key.append(byte_value)
            except ValueError as err:
                raise InvalidKeyError(f'Value could not be parsed as an integer in line {linenum} of key file')
            except IndexError as err:
                raise InvalidKeyError(f'Value missing in line {linenum} of key file')
    return key
