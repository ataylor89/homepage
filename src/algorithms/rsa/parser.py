from algorithms.exceptions import KeyFileError

def parse_key(path):
    key = []
    with open(path, 'r') as file:
        for index, line in enumerate(file):
            linenum = index + 1
            try:
                tokens = line.split()
                n, e, d = int(tokens[0][2:]), int(tokens[1][2:]), int(tokens[2][2:])
                key.append((n, e, d))
            except ValueError as err:
                raise KeyFileError(f'Value could not be parsed as an integer in line {linenum} of key file')
            except IndexError as err:
                raise KeyFileError(f'Value missing in line {linenum} of key file')
    return key
