from flask import Flask
from homepage import keys

app = Flask(__name__)
keys.load()

from homepage import views
