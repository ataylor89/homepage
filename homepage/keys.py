from algorithms.rsa import primetable as rsa_primetable
from algorithms.rsa import keytable as rsa_keytable
from algorithms.rsa import keygen as rsa_keygen
from algorithms.rsa import keyio as rsa_keyio
from algorithms.xor import keygen as xor_keygen
from algorithms.xor import keyio as xor_keyio
import os
import sys

keys = {'RSA': {}, 'XOR': {}}

def load():
    project_root = sys.path[0]

    path = f'{project_root}/algorithms/rsa/keys/'
    try:
        os.makedirs(path, exist_ok=False)
        print('Created directory ' + path)
    except: pass

    if os.path.isfile(path + 'default.txt'):
        try:
            keys['RSA']['default'] = rsa_keyio.load(path + 'default.txt')
            print(f'Loaded key from file {path}default.txt')
        except Exception as err:
            print(err)

    if 'default' not in keys['RSA'] or keys['RSA']['default'] is None:
        rsa_primetable.load()
        rsa_keytable.load()
        rsa_primetable.generate(1000)
        rsa_keytable.generate(64, 10, 1000)
        rsa_primetable.save()
        rsa_keytable.save()
        keys['RSA']['default'] = rsa_keygen.create_key_pair(64, 10, 1000)
        rsa_keyio.save(keys['RSA']['default'], path + 'default.txt')
        print(f'Saved key to file {path}default.txt')

    path = f'{project_root}/algorithms/xor/keys/'
    try:
        os.makedirs(path, exist_ok=False)
        print('Created directory ' + path)
    except: pass

    if os.path.isfile(path + 'default.txt'):
        try:
            keys['XOR']['default'] = xor_keyio.load(path + 'default.txt')
            print(f'Loaded key from file {path}default.txt')
        except Exception as err:
            print(err)

    if 'default' not in keys['XOR'] or keys['XOR']['default'] is None:
        keys['XOR']['default'] = xor_keygen.create_key(1024)
        xor_keyio.save(keys['XOR']['default'], path + 'default.txt')
        print(f'Saved key to file {path}default.txt')
