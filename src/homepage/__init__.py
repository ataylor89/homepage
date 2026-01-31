from homepage.key_manager import KeyManager
from flask import Flask

keys = KeyManager()
keys.load()

key_names = {}
sort_key = lambda x: (x != 'default', x)
key_names['rsa'] = sorted(keys['rsa'].keys(), key=sort_key)
key_names['xor'] = sorted(keys['xor'].keys(), key=sort_key)

app = Flask(__name__)
print('[homepage] Welcome to the homepage web application')

from homepage import views
