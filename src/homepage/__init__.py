from homepage.key_manager import KeyManager
from pathlib import Path
from flask import Flask

project_root = Path(__file__).parent.parent.parent

keys = KeyManager(project_root)
keys.load()

key_names = {}
key_names['rsa'] = sorted(keys['rsa'].keys())
key_names['xor'] = sorted(keys['xor'].keys())

app = Flask(__name__)
print('[homepage] Welcome to the homepage web application')

from homepage import views
