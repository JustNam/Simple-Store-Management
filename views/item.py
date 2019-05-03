from app import app
from flask import jsonify, g
from flask_jwt import jwt_required
from models.item import ItemModel
from utilities import message
from flask_expects_json import expects_json

schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string', 'maxLength': 255},
        'price': {'type': 'number'}
    },
    'required': ['name', 'price']
}


@app.route('/items', methods=['GET'])
@jwt_required()
def get_items():
    items = ItemModel.query.all()
    items = [item.to_dict()
             for item in items]
    return jsonify(items)


@app.route('/items/<int:_id>', methods=['GET'])
@jwt_required()
def get_item(_id):
    item = ItemModel.find_item_by_id(_id)
    if item:
        return jsonify(item.to_dict())
    return message("There is no item whose id is equal {}".format(_id), 400)


@app.route('/items', methods=["POST"])
@expects_json(schema)
@jwt_required()
def create_item():
    # Get item data from the request
    new_item = ItemModel.create_from_dict(g.data)
    new_item.save_to_db()
    return jsonify(new_item.to_dict()), 201


@app.route('/items/<int:_id>', methods=["PUT"])
@expects_json(schema)
@jwt_required()
def update_item(_id):
    item = ItemModel.find_item_by_id(_id)
    if item:
        # The item already exists
        item.update_from_dict(g.data)
        item.update_to_db()
        return jsonify(item.to_dict()), 200
    item = ItemModel.create_from_dict(g.data)
    item.save_to_db()
    return jsonify(item.to_dict()), 201


@app.route('/items/<int:_id>', methods=["DELETE"])
@jwt_required()
def delete_item(_id):
    item = ItemModel.find_item_by_id(_id)
    if item:
        name = item.name
        item.delete_from_db()
        return message('The {} was deleted from database'.format(name), 200)
    return message("There is no item whose id is equal {}".format(_id), 400)
