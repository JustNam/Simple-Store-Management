from db import db


class StoreModel(db.Model):
    __tablename__ = "stores"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    items = db.relationship('ItemModel', lazy="dynamic", backref='store')

    def __init__(self, name):
        self.name = name

    @classmethod
    def create_from_dict(cls, _dict):
        return cls(_dict['name'])

    def to_dict(self):
        return {"name": self.name, "items": [item.to_dict() for item in self.items]}

    def update_from_dict(self, dic):
        if 'name' in dic:
            self.name = dic['name']

    @classmethod
    def find_store_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_store_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update_to_db(self):
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
