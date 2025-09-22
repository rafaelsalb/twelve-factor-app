from marshmallow import Schema, fields

from .post import PostSchema


class UserSchema(Schema):
    id = fields.Int()
    username = fields.String()
    email = fields.String()
    posts = fields.List(fields.Nested(PostSchema))
