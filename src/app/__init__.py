from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    application = Flask(__name__)
    application.config.from_object(Config)
    db.init_app(application)
    migrate.init_app(application)

    from . import routes

    application.register_blueprint(routes.bp)

    return application
