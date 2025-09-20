from flask import Blueprint

bp = Blueprint("index", __name__, url_prefix="")


@bp.get("/")
def index():
    return "Hello, world!"
