from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os.path import expanduser
import os
import config
from config import config


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    print(config_name)
    print("AAAAAAAAAAAAA: " + str(os.environ.get('DEV_DATABASE_URL')))
    # print(os.environ['APP_SETTINGS'])
    # app.config.update('SQLALCHEMY_DATABASE_URI', 'sqlite:///' + expanduser('~') + '/app/database.db')
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + expanduser('~') + '/app/database.db'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SECRET_KEY'] = "paw"
    # app.config['DEBUG'] = True

    print(app.config.get('SQLALCHEMY_DATABASE_URI'))

    from app import basicServer
    app.register_blueprint(basicServer.login_bp)
    app.register_blueprint(basicServer.book_bp)

    db.init_app(app)  # type:SQLAlchemy

    return app
