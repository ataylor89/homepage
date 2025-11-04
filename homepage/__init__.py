from flask import Flask
from homepage import keys

app = Flask(__name__)
print('[homepage] Welcome to the homepage web application')
keys.load()

from homepage import views
