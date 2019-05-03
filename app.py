from flask import Flask, jsonify, request
from flask_jwt import JWT
from sercurity import authenticate, identify
import os


# Name of the main module
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'hodns'

jwt = JWT(app, authenticate, identify)

import views.item
import views.user
import views.store