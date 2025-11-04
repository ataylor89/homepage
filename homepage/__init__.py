from flask import Flask
from homepage import keys

app = Flask(__name__)
print('[homepage] Welcome to the homepage web app')
keys.load()

from homepage import views
