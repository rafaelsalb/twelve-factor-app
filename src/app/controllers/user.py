import sqlalchemy as sa
from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, verify_jwt_in_request

from .. import db
from ..models.user import User
from ..schemas.user import UserSchema

bp = Blueprint("user", __name__, url_prefix="/user")


@bp.get("")
def get_all():
    users = User.query.all()
    return jsonify(UserSchema(many=True).dump(users))


@bp.get("/<id>")
def get(id):
    user = User.query.get(id)

    if user is None:
        return {"message": "User not found."}, 404

    return jsonify(UserSchema().dump(user))
