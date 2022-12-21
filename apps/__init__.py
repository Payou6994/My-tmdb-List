import os
from importlib import import_module

# import flask_sijax
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from tmdb import tmdb

tmdb.from_json = os.getenv("FROM_JSON")
db = SQLAlchemy()
login_manager = LoginManager()
supported_languages = ["fr-FR", "en-US"]


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)


def register_blueprints(app):
    for module_name in ("authentication", "home"):
        module = import_module("apps.{}.routes".format(module_name))
        app.register_blueprint(module.blueprint)


def configure_database(app):
    @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def create_app(config):
    app = Flask(__name__)
    # flask_sijax.Sijax(app)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    configure_database(app)
    return app
