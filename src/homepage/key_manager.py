from settings import project_root
from algorithms.rsa import parser as rsa_parser
from algorithms.xor import parser as xor_parser
from algorithms.exceptions import KeyFileError

class KeyManager(dict):

    def __init__(self):
        super().__init__()
        self['rsa'] = {}
        self['xor'] = {}

    def load(self):
        rsa_folder = project_root / 'keys' / 'rsa'
        xor_folder = project_root / 'keys' / 'xor'

        for path in rsa_folder.iterdir():
            if path.is_file() and path.suffix == '.txt':
                keyname = path.stem
                try:
                    self['rsa'][keyname] = rsa_parser.parse_key(path)
                    print(f'[homepage] Loaded key {path}')
                except KeyFileError as err:
                    print(err)

        for path in xor_folder.iterdir():
            if path.is_file() and path.suffix == '.txt':
                keyname = path.stem
                try:
                    self['xor'][keyname] = xor_parser.parse_key(path)
                    print(f'[homepage] Loaded key {path}')
                except KeyFileError as err:
                    print(err)
