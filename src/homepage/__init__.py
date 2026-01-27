from homepage.key_manager import KeyManager
from flask import Flask

keys = KeyManager()
keys.load()

key_names = {}
key_names['rsa'] = sorted(keys['rsa'].keys())
key_names['xor'] = sorted(keys['xor'].keys())

app = Flask(__name__)
print('[homepage] Welcome to the homepage web application')

from homepage import views
