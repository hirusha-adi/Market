
import urllib.parse
from pymongo import MongoClient
from database.settings import Mongo
from bson import ObjectId

client = MongoClient('mongodb://%s:%s@%s:27017/' %
                     (
                         urllib.parse.quote_plus(Mongo.username),
                         urllib.parse.quote_plus(Mongo.password),
                         Mongo.ip
                     )
                     )

users = client['Market']['users']


class Users:
    """
    {
        "_id": {
            "$oid": ""
        },
        "id": 1,
        "username": "",
        "password": "",
        "name": "",
        "phone": "",
        "city": ""
    }
    """

    def getAllUsers():
        temp = []
        for user in users.find({}):
            temp.append(user)
        print(temp)
        return temp

    def addUser():
        pass
