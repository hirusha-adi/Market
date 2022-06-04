
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
    pass
