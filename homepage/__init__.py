from flask import Flask
from homepage import keys
import sys

app = Flask(__name__)
project_root = sys.path[0]
keys.load()

from homepage import views
