from algorithms.rsa import parser as rsa_parser
from algorithms.xor import parser as xor_parser
from algorithms.exceptions import KeyFileError
import os

class KeyManager(dict):

    def __init__(self, project_root):
        super().__init__()
        self.project_root = project_root
        self['rsa'] = {}
        self['xor'] = {}

    def load(self):
        rsa_folder = self.project_root / 'keys' / 'rsa'
        xor_folder = self.project_root / 'keys' / 'xor'

        for filename in os.listdir(rsa_folder):
            path = rsa_folder / filename
            if path.is_file() and filename.endswith('.txt'):
                keyname = filename[:-4]
                try:
                    self['rsa'][keyname] = rsa_parser.parse_key(path)
                    print(f'[homepage] Loaded key {path}')
                except KeyFileError as err:
                    print(err)

        for filename in os.listdir(xor_folder):
            path = xor_folder / filename
            if path.is_file() and filename.endswith('.txt'):
                keyname = filename[:-4]
                try:
                    self['xor'][keyname] = xor_parser.parse_key(path)
                    print(f'[homepage] Loaded key {path}')
                except KeyFileError as err:
                    print(err)
