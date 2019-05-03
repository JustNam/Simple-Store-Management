from app import app
from flask import g, jsonify
from models.user import UserModel
from utilities import message
from flask_expects_json import expects_json

schema = {
    'type': 'object',
    'properties': {
        'username': {'type': 'string', 'maxLength': 50},
        'password': {'type': 'string', 'maxLength': 120}
    },
    'required': ['username', 'password']
}


@app.route('/register', methods=["POST"])
@expects_json(schema)
def create_user():
    new_user = UserModel.create_from_dict(g.data)
    new_user.save_to_db()
    return message("User {} was created".format(new_user.username), 201)
