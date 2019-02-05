from flask import Flask
from os.path import expanduser
from flask_sqlalchemy import SQLAlchemy



JSON_MIME_TYPE = 'application/json'

app = Flask(__name__)


app.debug = True
app.testing = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + expanduser('~') + '/app/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "paw"

db = SQLAlchemy(app)  # type: SQLAlchemy
