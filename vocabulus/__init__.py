from flask import Flask
from vocabulus.config import SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

from vocabulus import routes
