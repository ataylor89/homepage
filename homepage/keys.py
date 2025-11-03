from algorithms.rsa import primetable as rsa_primetable
from algorithms.rsa import keytable as rsa_keytable
from algorithms.rsa import keygen as rsa_keygen
from algorithms.rsa import keyio as rsa_keyio
from algorithms.xor import keygen as xor_keygen
from algorithms.xor import keyio as xor_keyio
import os
import sys

keys = {
    'RSA': {'small': None, 'medium': None, 'large': None},
    'XOR': {'small': None, 'medium': None, 'large': None}
}

def init():
    project_root = sys.path[0]
    path = f'{project_root}/algorithms/rsa/keys'
    try:
        os.makedirs(path, exist_ok=False)
        print('Created directory ' + path)
    except: pass
    path = f'{project_root}/algorithms/xor/keys'
    try:
        os.makedirs(path, exist_ok=False)
        print('Created directory ' + path)
    except: pass

def load_from_files():
    project_root = sys.path[0]
    path = f'{project_root}/algorithms/rsa/keys'

    counts = [0, 0]

    if os.path.isfile(path + 'small.txt'):
        try:
            keys['RSA']['small'] = rsa_keyio.load(path + 'small.txt')
            counts[0] += 1
            print('Successfully loaded keyfile %s' %(path + 'small.txt'))
        except Exception as err:
            print(err)

    if os.path.isfile(path + 'medium.txt'):
        try:
            keys['RSA']['medium'] = rsa_keyio.load(path + 'medium.txt')
            counts[0] += 1
            print('Successfully loaded keyfile %s' %(path + 'medium.txt'))
        except Exception as err:
            print(err)

    if os.path.isfile(path + 'large.txt'):
        try:
            keys['RSA']['large'] = rsa_keyio.load(path + 'large.txt')
            counts[0] += 1
            print('Successfully loaded keyfile %s' %(path + 'large.txt'))
        except Exception as err:
            print(err)

    path = f'{project_root}/algorithms/xor/keys'

    if os.path.isfile(path + 'small.txt'):
        try:
            keys['XOR']['small'] = xor_parser.parse_key(path + 'small.txt')
            counts[1] += 1
            print('Successfully loaded keyfile %s' %(path + 'small.txt'))
        except Exception as err:
            print(err)

    if os.path.isfile(path + 'medium.txt'):
        try:
            keys['XOR']['medium'] = xor_parser.parse_key(path + 'medium.txt')
            counts[1] += 1
            print('Successfully loaded keyfile %s' %(path + 'medium.txt'))
        except Exception as err:
            print(err)

    if os.path.isfile(path + 'large.txt'):
        try:
            keys['XOR']['large'] = xor_parser.parse_key(path + 'large.txt')
            counts[1] += 1
            print('Successfully loaded keyfile %s' %(path + 'large.txt'))
        except Exception as err:
            print(err)

    return counts

def load():
    init()
    counts = load_from_files()
    project_root = sys.path[0]

    if counts[0] < 3:
        path = f'{project_root}/algorithms/rsa/keys/'
        rsa_primetable.load()
        rsa_keytable.load()
        rsa_primetable.generate(1000)
        rsa_keytable.generate(64, 10, 1000)
        rsa_keytable.generate(64, 100, 1000)
        rsa_keytable.generate(64, 500, 1000)
        rsa_primetable.save()
        rsa_keytable.save()
        if not keys['RSA']['small']:
            keys['RSA']['small'] = rsa_keygen.create_key_pair(64, 10, 1000)
            rsa_keyio.save(keys['RSA']['small'], path + 'small.txt')
            print(f'Created file {path}small.txt')
        if not keys['RSA']['medium']:
            keys['RSA']['medium'] = rsa_keygen.create_key_pair(64, 100, 1000)
            rsa_keyio.save(keys['RSA']['medium'], path + 'medium.txt')
            print(f'Created file {path}medium.txt')
        if not keys['RSA']['large']:
            keys['RSA']['large'] = rsa_keygen.create_key_pair(64, 500, 1000)
            rsa_keyio.save(keys['RSA']['large'], path + 'large.txt')
            print(f'Created file {path}large.txt')
    if counts[1] < 3:
        path = f'{project_root}/algorithms/xor/keys/'
        if not keys['XOR']['small']:
            keys['XOR']['small'] = xor_keygen.create_key(64)
            xor_keyio.save(keys['XOR']['small'], path + 'small.txt')
            print(f'Created file {path}small.txt')
        if not keys['XOR']['medium']:
            keys['XOR']['medium'] = xor_keygen.create_key(256)
            xor_keyio.save(keys['XOR']['medium'], path + 'medium.txt')
            print(f'Created file {path}medium.txt')
        if not keys['XOR']['large']:
            keys['XOR']['large'] = xor_keygen.create_key(1024)
            xor_keyio.save(keys['XOR']['large'], path + 'large.txt')
            print(f'Created file {path}large.txt')
