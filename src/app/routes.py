from flask import Blueprint, current_app

from .controllers import auth, post, user

bp = Blueprint("index", __name__, url_prefix="")


@bp.get("/")
def index():
    return "Hello, world!"


def register_blueprints(app):
    """
    Register all blueprints here.
    """
    app.register_blueprint(bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(post.bp)
    app.register_blueprint(user.bp)
