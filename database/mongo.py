
import urllib.parse
from pymongo import MongoClient
# from database.settings import Mongo
from bson import ObjectId


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
        return temp

    def getLastUser():
        temp = []
        for user in users.find().sort([('timestamp', -1)]).limit(1):
            temp.append(user)
        return temp

    def getUserByUsername(username: str):
        temp = []
        for user in users.find({'username': username}):
            temp.append(user)
        return temp

    def getUserByName(name: str):
        temp = []
        for user in users.find(
            {
                "name": {
                    "$regex": f'.*{name}*.',
                    "$options": 'i'  # ignore case
                }
            }
        ):
            temp.append(user)
        return temp

    def addUser(username, password, name, phone, city):
        users.insert_one(
            {
                'username': username,
                'password': password,
                'name': name,
                'phone': phone,
                'city': city
            }
        )

    def updateUser(username, password, name, phone, city):
        temp = []
        for user in users.find(
            {
                "username": username
            },
            {
                "$set": {
                    'username': username,
                    'password': password,
                    'name': name,
                    'phone': phone,
                    'city': city
                }
            },
            upsert=True
        ):
            temp.append(user)
        return temp


x = Users.getUserByName()
print(x)
