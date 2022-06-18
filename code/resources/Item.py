from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required
from flask import Flask,request

from models.Item import ItemModel

from db import db

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float,required=True,help='Kindly enter the price field')
    parser.add_argument('store_id',type=int,required=True,help="Every item needs a store_id")
    
    @jwt_required()
    def get(self,name):
        item = ItemModel.find_by_item_name(name)
        if item:
            return item.json()
        return {'message':"item not found"},404
        
    
    def post(self,name):
        
        isItemExists = ItemModel.find_by_item_name(name)
        data = Item.parser.parse_args()
        print(isItemExists.name)
        print(isItemExists.store_id)

        if isItemExists.name == name and isItemExists.store_id == data['store_id']:
            return {"message":"Item with name '{}' already exists in the same store id {}".format(name,data['store_id'])},400

        item = ItemModel(name,data['price'],data['store_id'])

        try:
            item.save_to_db()
        except:
            return {"message":"Error occured on inserting the item"},500
        return item.json(),201
    
    def delete(self,name):
        item = ItemModel.find_by_item_name(name)
        if item:
            item.delete()
        return {'message':'Item Deleted'}

    def put(self,name):
        data = Item.parser.parse_args()
        item =ItemModel.find_by_item_name(name)
        if item is None:
            item =  ItemModel(name,data['price'],data['store_id'])
        else:
            item.price = data['price']
            try:
                item.save_to_db()
            except:
                return  {'message':'Error occurred while persisting the item'}, 500
        return item.json(),201


class ItemList(Resource):

    def get(self):
        return {'items':list(map(lambda x: x.json(), ItemModel.query.all()))}