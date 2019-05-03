from app import app
from flask import jsonify, g
from flask_jwt import jwt_required
from models.store import StoreModel
from utilities import message
from flask_expects_json import expects_json

schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string', 'maxLength': 255},
    },
    'required': ['name']
}


@app.route('/stores', methods=['GET'])
@jwt_required()
def get_stores():
    stores = StoreModel.query.all()
    stores = [store.to_dict()
              for store in stores]
    return jsonify(stores)


@app.route('/stores/<int:_id>', methods=['GET'])
@jwt_required()
def get_store(_id):
    store = StoreModel.find_store_by_id(_id)
    if store:
        return jsonify(store.to_dict())
    return message("There is no store whose id is equal {}".format(_id), 400)


@app.route('/stores', methods=["POST"])
@expects_json(schema)
@jwt_required()
def create_store():
    # Get store information from the request
    new_store = StoreModel.create_from_dict(g.data)
    new_store.save_to_db()
    return jsonify(new_store.to_dict()), 201


@app.route('/stores/<int:_id>', methods=["PUT"])
@expects_json(schema)
@jwt_required()
def update_store(_id):
    store = StoreModel.find_store_by_id(_id)
    if store:
        # The store already exists
        store.update_from_dict(g.data)
        store.update_to_db()
        return jsonify(store.to_dict()), 201
    store.save_to_db()
    return jsonify(store.to_dict()), 200


@app.route('/stores/<int:_id>', methods=["DELETE"])
@jwt_required()
def delete_store(_id):
    store = StoreModel.find_store_by_id(_id)
    if store:
        name = store.name
        store.delete_from_db()
        return message('The {} was deleted from database'.format(name), 200)
    return message("There is no store whose id is equal {}".format(_id), 400)