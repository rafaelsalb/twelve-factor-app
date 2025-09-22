import sqlalchemy as sa
from flask import Blueprint, request
from flask_jwt_extended import create_access_token

from .. import db
from ..models.user import User

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.post("/login")
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).one_or_none()
    if user is None:
        return {"message": f"No user with username {username}."}
    if user.check_password(password):
        token = create_access_token(identity=username)
        return {"message": "Login successful.", "token": token}
    else:
        return {"message": "Invalid credentials."}, 401


@bp.post("/register")
def register():
    data = request.json
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    user = User(username=username, email=email)
    user.set_password(password)

    db.session.add(user)
    try:
        db.session.commit()
    except sa.exc.IntegrityError:
        return {"message": f"An user with the username '{username}' already exists."}

    return {"message": "User created successfully."}, 201
