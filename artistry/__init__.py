from flask import Flask

app = Flask(__name__)

from artistry.views import main
