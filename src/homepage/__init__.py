from flask import Flask

app = Flask(__name__)
print('[homepage] Welcome to the homepage web application')

from homepage import views
