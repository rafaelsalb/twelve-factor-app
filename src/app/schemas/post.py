from marshmallow import Schema, fields


class PostSchema(Schema):
    id = fields.Int()
    content = fields.String()
    creation_date = fields.DateTime()
    update_date = fields.DateTime()
    user_id = fields.Int()


class CreatePostSchema(Schema):
    content = fields.String(load_only=True)


class UpdatePostSchema(Schema):
    content = fields.String(load_only=True)
