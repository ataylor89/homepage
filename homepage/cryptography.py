from algorithms.rsa import encrypt, decrypt, parser
from algorithms.xor import xor
from algorithms import rot13, rot88

key_paths = {
    'RSA': {
        'small': 'algorithms/rsa/keys/small.txt',
        'medium': 'algorithms/rsa/keys/medium.txt',
        'large': 'algorithms/rsa/keys/large.txt',
        'default': 'algorithms/rsa/keys/large.txt'
    },
    'XOR': {
        'small': 'algorithms/xor/keys/small.txt',
        'medium': 'algorithms/xor/keys/medium.txt',
        'large': 'algorithms/xor/keys/large.txt',
        'default': 'algorithms/xor/keys/default.txt'
    }
}

def crypt(algorithm, key_name, message, action):
    if algorithm == 'RSA':
        if key_name in key_paths['RSA']:
            key_path = key_paths['RSA'][key_name]
            if action == 'encrypt':
                key = parser.parse_key(key_path)
                ciphertext = encrypt.encrypt(message, key)
                hexstr = ciphertext.encode('utf-8').hex()
                return hexstr
            elif action == 'decrypt':
                key = parser.parse_key(key_path)
                ciphertext = bytes.fromhex(message).decode('utf-8')
                plaintext = decrypt.decrypt(ciphertext, key)
                return plaintext
    elif algorithm == 'XOR':
        if key_name in key_paths['XOR']:
            key_path = key_paths['XOR'][key_name]
            xor_keyfile = open(key_path, 'r')
            xor_key = xor_keyfile.read()
            if action == 'encrypt':
                ciphertext = xor.crypt(message, xor_key)
                hexstr = ciphertext.encode('utf-8').hex()
                return hexstr
            elif action == 'decrypt':
                ciphertext = bytes.fromhex(message).decode('utf-8')
                plaintext = xor.crypt(ciphertext, xor_key)
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
