from algorithms import rot13, rot88
from algorithms.rsa import encrypt, decrypt, parser as rsa_parser
from algorithms.xor import xor, parser as xor_parser
from homepage import project_root, defaults

paths = {
    'RSA': {
        'small': f'{project_root}/algorithms/rsa/keys/small.txt',
        'medium': f'{project_root}/algorithms/rsa/keys/medium.txt',
        'large': f'{project_root}/algorithms/rsa/keys/large.txt',
    },
    'XOR': {
        'small': f'{project_root}/algorithms/xor/keys/small.txt',
        'medium': f'{project_root}/algorithms/xor/keys/medium.txt',
        'large': f'{project_root}/algorithms/xor/keys/large.txt',
    }
}

def get_key(name, type):
    if type == 'RSA':
        if name in paths:
            path = paths['RSA'][key_name]
            try:
                return rsa_parser.parse_key(path)
            except Exception as err:
                print(err)
        return defaults.rsa_key
    elif type == 'XOR':
        if name in paths:
            path = paths['XOR'][name]
            try:
                return xor_parser.parse_key(path)
            except Exception as err:
                print(err)
        return defaults.xor_key

def crypt(algorithm, key_name, message, action):
    if algorithm == 'RSA':
        if action == 'encrypt':
            key = get_key(key_name, 'RSA')
            ciphertext = encrypt.encrypt(message, key)
            hexstr = ciphertext.encode('utf-8').hex()
            return hexstr
        elif action == 'decrypt':
            key = get_key(key_name, 'RSA')
            ciphertext = bytes.fromhex(message).decode('utf-8')
            plaintext = decrypt.decrypt(ciphertext, key)
            return plaintext
    elif algorithm == 'XOR':
        if action == 'encrypt':
            key = get_key(key_name, 'XOR')
            ciphertext = xor.crypt(message, key)
            hexstr = ciphertext.encode('utf-8').hex()
            return hexstr
        elif action == 'decrypt':
            key = get_key(key_name, 'XOR')
            ciphertext = bytes.fromhex(message).decode('utf-8')
            plaintext = xor.crypt(ciphertext, key)
            return plaintext
    elif algorithm == 'ROT13':
        return rot13.rot13(message)
    elif algorithm == 'ROT88':
        if action == 'encrypt':
            ciphertext = rot88.rot88(message)
            hexstr = ciphertext.encode('utf-8').hex()
            return hexstr
        elif action == 'decrypt':
            ciphertext = bytes.fromhex(message).decode('utf-8')
            plaintext = rot88.rot88(ciphertext)
            return plaintext
