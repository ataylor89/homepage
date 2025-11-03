from algorithms import rot13, rot88
from algorithms.rsa import encrypt, decrypt
from algorithms.xor import xor
from homepage.keys import keys

def crypt(algorithm, key_name, message, action):
    if algorithm == 'RSA':
        key = keys['RSA'][key_name]
        if action == 'encrypt':
            ciphertext = encrypt.encrypt(message, key)
            hexstr = ciphertext.encode('utf-8').hex()
            return hexstr
        elif action == 'decrypt':
            ciphertext = bytes.fromhex(message).decode('utf-8')
            plaintext = decrypt.decrypt(ciphertext, key)
            return plaintext
    elif algorithm == 'XOR':
        key = keys['XOR'][key_name]
        if action == 'encrypt':
            ciphertext = xor.crypt(message, key)
            hexstr = ciphertext.encode('utf-8').hex()
            return hexstr
        elif action == 'decrypt':
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
