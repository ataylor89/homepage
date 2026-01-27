from homepage import keys
from algorithms import rot13, rot88, md5, sha256
from algorithms.rsa import encrypt, decrypt
from algorithms.xor import xor

def crypt(algorithm, key_name, message, action):
    if algorithm == 'rsa':
        key = keys['rsa'][key_name]
        if action == 'encrypt':
            ciphertext = encrypt.encrypt(message, key)
            hexstr = ciphertext.encode('utf-8').hex()
            return hexstr
        elif action == 'decrypt':
            ciphertext = bytes.fromhex(message).decode('utf-8')
            plaintext = decrypt.decrypt(ciphertext, key)
            return plaintext
    elif algorithm == 'xor':
        key = keys['xor'][key_name]
        if action == 'encrypt':
            ciphertext = xor.crypt(message, key)
            hexstr = ciphertext.encode('utf-8').hex()
            return hexstr
        elif action == 'decrypt':
            ciphertext = bytes.fromhex(message).decode('utf-8')
            plaintext = xor.crypt(ciphertext, key)
            return plaintext
    elif algorithm == 'rot13':
        return rot13.rot13(message)
    elif algorithm == 'rot88':
        if action == 'encrypt':
            ciphertext = rot88.rot88(message)
            hexstr = ciphertext.encode('utf-8').hex()
            return hexstr
        elif action == 'decrypt':
            ciphertext = bytes.fromhex(message).decode('utf-8')
            plaintext = rot88.rot88(ciphertext)
            return plaintext
    elif algorithm == 'md5':
        return md5.md5(message.encode('utf-8')).hexdigest
    elif algorithm == 'sha256':
        return sha256.sha256(message.encode('utf-8')).hexdigest
