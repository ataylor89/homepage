import os
import sys
from algorithms.rsa import primetable as rsa_primetable
from algorithms.rsa import keytable as rsa_keytable
from algorithms.rsa import keygen as rsa_keygen
from algorithms.rsa import keyio as rsa_keyio
from algorithms.xor import keygen as xor_keygen
from algorithms.xor import keyio as xor_keyio

keys = {'RSA': {}, 'XOR': {}}

def load():
    project_root = sys.path[0]
    rsa_key_path = f'{project_root}/algorithms/rsa/keys/'
    xor_key_path = f'{project_root}/algorithms/xor/keys/'

    try:
        os.makedirs(rsa_key_path, exist_ok=False)
        print('Created directory ' + rsa_key_path)
    except: pass

    try:
        os.makedirs(xor_key_path, exist_ok=False)
        print('Created directory ' + xor_key_path)
    except: pass

    for item in os.listdir(rsa_key_path):
        full_path = os.path.join(rsa_key_path, item)
        if os.path.isfile(full_path) and item.endswith('.key'):
            keyname = item[:-4]
            try:
                keys['RSA'][keyname] = rsa_keyio.load(full_path)
                print(f'Loaded key from file {full_path}')
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
        rsa_keyio.save(keys['RSA']['default'], rsa_key_path + 'default.key')
        print(f'Saved key to file {rsa_key_path}default.key')

    for item in os.listdir(xor_key_path):
        full_path = os.path.join(xor_key_path, item)
        if os.path.isfile(full_path) and item.endswith('.key'):
            keyname = item[:-4]
            try:
                keys['XOR'][keyname] = xor_keyio.load(full_path)
                print(f'Loaded key from file {full_path}')
            except Exception as err:
                print(err)

    if 'default' not in keys['XOR'] or keys['XOR']['default'] is None:
        keys['XOR']['default'] = xor_keygen.create_key(1024)
        xor_keyio.save(keys['XOR']['default'], xor_key_path + 'default.key')
        print(f'Saved key to file {xor_key_path}default.key')

def get_key_names():
    rsa_key_names = sorted(list(keys['RSA'].keys()))
    xor_key_names = sorted(list(keys['XOR'].keys()))
    return {'RSA': rsa_key_names, 'XOR': xor_key_names}
