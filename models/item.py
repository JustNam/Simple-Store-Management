from db import db


class ItemModel(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=False)

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    @classmethod
    def create_from_dict(cls, _dict):
        return cls(_dict['name'], _dict['price'], _dict['store_id'])

    def to_dict(self):
        return {"name": self.name, "price": self.price}

    def update_from_dict(self, dic):
        if 'name' in dic:
            self.name = dic['name']
        if 'price' in dic:
            self.price = dic['price']
        if 'name' in dic:
            self.store_id = dic['store_id']

    @classmethod
    def find_item_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_item_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update_to_db(self):
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
