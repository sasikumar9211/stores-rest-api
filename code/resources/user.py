from flask_restful import Resource, reqparse
from db import db
from models.user import UserModel


class UserRegister(Resource):
   
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str,required=True,help='Kindly enter the username field')
    parser.add_argument('password', type=str,required=True,help='Kindly enter the password field')

    def post(Self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message":"User already exists with the same name"},400

        user =UserModel(**data)
        user.save_to_db()
        return {"message":"User Created Successfully"},201