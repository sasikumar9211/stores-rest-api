import os
from flask import Flask,request
from flask_restful import Resource,Api, reqparse
from flask_jwt import JWT, jwt_required

from resources.user import UserRegister

from security import authenticate, identity

from resources.Item import Item,ItemList

from resources.store import Store,StoreList

app = Flask(__name__)

#uri = os.environ.get('DATABASE_URL', 'sqlite:///data.db')

uri = os.getenv('DATABASE_URL')

if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False
app.secret_key ='jose'
api =Api(app)

jwt =JWT(app, authenticate,identity)


api.add_resource(ItemList,'/items')
api.add_resource(Item,"/item/<string:name>")
api.add_resource(UserRegister,"/register")
api.add_resource(Store,"/store/<string:name>")
api.add_resource(StoreList,"/stores")

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    
    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)