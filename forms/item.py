from wtforms import Form, StringField, IntegerField, validators, ValidationError
from flask_wtf import FlaskForm


class ItemForm(FlaskForm):
    name = StringField("name")
    price = IntegerField("price")