from algorithms.rsa import parser as rsa_parser
from algorithms.xor import parser as xor_parser
from algorithms.exceptions import InvalidKeyError
import sys
import os

class KeyManager(dict):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['rsa'] = {}
        self['xor'] = {}

    def load(self):
        base_dir = sys.path[0]
        rsa_key_folder = f'{base_dir}/keys/rsa'
        xor_key_folder = f'{base_dir}/keys/xor'

        for item in os.listdir(rsa_key_folder):
            path = os.path.join(rsa_key_folder, item)
            if os.path.isfile(path) and item.endswith('.txt'):
                keyname = item[:-4]
                try:
                    self['rsa'][keyname] = rsa_parser.parse_key(path)
                    print(f'[homepage] Loaded key {path}')
                except InvalidKeyError as err:
                    print('InvalidKeyError: %s' %err)

        for item in os.listdir(xor_key_folder):
            path = os.path.join(xor_key_folder, item)
            if os.path.isfile(path) and item.endswith('.txt'):
                keyname = item[:-4]
                try:
                    self['xor'][keyname] = xor_parser.parse_key(path)
                    print(f'[homepage] Loaded key {path}')
                except InvalidKeyError as err:
                    print('InvalidKeyError: %s' %err)
