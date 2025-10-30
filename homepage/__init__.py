from flask import Flask
app = Flask(__name__)

import sys
project_root = sys.path[0]

from homepage import views
