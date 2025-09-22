from flask import Blueprint, jsonify, request
from flask_jwt_extended import current_user, jwt_required

from .. import db
from ..models.post import Post
from ..schemas.post import CreatePostSchema, PostSchema, UpdatePostSchema

bp = Blueprint("post", __name__, url_prefix="/post")


@bp.get("")
def get_all():
    posts = Post.query.order_by(Post.creation_date.desc()).all()
    return jsonify(PostSchema(many=True).dump(posts))


@bp.get("/<id>")
def get(id):
    post = Post.query.get(id)

    if post is None:
        return {"message": "Post not found."}, 404

    return jsonify(PostSchema().dump(post))


@bp.post("")
@jwt_required()
def create():
    data = CreatePostSchema().load(request.json)
    content = data.get("content")
    try:
        post = Post(content=content, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
    except Exception:
        db.session.rollback()
        return {"message": "Something went wrong while creating the post."}, 400
    return jsonify(PostSchema().dump(post))


@bp.put("/<id>")
@jwt_required()
def update(id):
    data = UpdatePostSchema().load(request.json)
    content = data.get("content")
    try:
        post = Post.query.get(id)

        if post is None:
            return {"message": "Post not found."}, 404

        if post.author.id == current_user.id:
            post.content = content
            db.session.commit()
        else:
            return {"message": "You are not the author of the post."}, 401
    except Exception:
        db.session.rollback()
        return {"message": "Something went wrong while updating the post."}, 400
    return jsonify(PostSchema().dump(post))
