
import urllib.parse
from pymongo import MongoClient
import pymongo
# from database.settings import Mongo
from bson import ObjectId

client = MongoClient('mongodb://%s:%s@%s:27017/' %
                     (
                         urllib.parse.quote_plus("marketadmin"),
                         urllib.parse.quote_plus("xa_zK$CeJ8[W(n@a"),
                         "45.142.214.184"
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
        return temp

    def getLastUser():
        """
        This is improvable and i dont know how to with pymongo
            https://stackoverflow.com/questions/32076382/mongodb-how-to-get-max-value-from-collections
        """
        temp = []
        for user in Users.getAllUsers():
            temp.append(user)
        return temp[-1]

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
        users.find_one_and_update(
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
        )
        return True


x = Users.getLastUser()
print(x)
