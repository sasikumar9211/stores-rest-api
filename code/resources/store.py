

from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):

    def get(self,name):
        store = StoreModel.find_by_name(name)

        if store:
            return store.json()
        
        return {"message": "Store not found"},404
    

    def post(self,name):
        store = StoreModel.find_by_name(name)

        if store:
            return {"message":"Store with a name {} already exists.".format(name)}

        newStore =StoreModel(name)

        try:
            newStore.save_to_db()
        except:
            return {"message":"Error occurred while inserting the record"}
        
        return newStore.json()
    

    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete()
        return {"message":"Items Deleted"}


class StoreList(Resource):

    def get(self):
        return {"stores":list(map(lambda x: x.json(), StoreModel.query.all()))}
            