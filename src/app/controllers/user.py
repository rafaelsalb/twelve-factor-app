import sqlalchemy as sa
from flask import Blueprint, jsonify, request
from flask_jwt_extended import (
    create_access_token,
    current_user,
    jwt_required,
    verify_jwt_in_request,
)

from .. import db
from ..models.user import User
from ..schemas.user import UpdateUserSchema, UserSchema

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


@bp.put("/<id>")
@jwt_required()
def update(id):
    try:
        if int(id) != current_user.id:
            return {"message": "You can only update your own profile."}, 401

        user = User.query.get(id)

        if user is None:
            return {"message": "User not found."}, 404

        data = UpdateUserSchema().load(request.json)
        email = data.get("email")
        user.email = email

        db.session.commit()
    except Exception:
        db.session.rollback()
        return {"message": "Something went wrong updating the user."}, 400
    return jsonify(UserSchema().dump(user)), 200


@bp.delete("/<id>")
@jwt_required()
def delete(id):
    try:
        if int(id) != current_user.id:
            return {"message": "You can only delete your own profile."}, 401

        user = User.query.get(id)

        if user is None:
            return {"message": "User not found."}, 404

        for post in user.posts:
            db.session.delete(post)

        db.session.delete(user)
        db.session.commit()
    except Exception:
        db.session.rollback()
        return {"message": "Something went wrong deleting the user."}, 400
    return jsonify(UserSchema().dump(user)), 200
