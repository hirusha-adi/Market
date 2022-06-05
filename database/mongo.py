
import urllib.parse
from pymongo import MongoClient
from database.settings import Mongo
from bson import ObjectId

client = MongoClient('mongodb://%s:%s@%s:27017/' % (
    urllib.parse.quote_plus(Mongo.username),
    urllib.parse.quote_plus(Mongo.password),
    Mongo.ip
))

users = client['Market']['users']
posts = client['Market']['posts']


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
        "email": "",
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
        return temp[0]

    def getUserByID(id):
        temp = []
        for user in users.find({'id': id}):
            temp.append(user)
        return temp[0]

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

    def addUser(username, password, name, phone, email, city):
        users.insert_one(
            {
                'id': int(Users.getLastUser()['id']) + 1,
                'username': username,
                'password': password,
                'name': name,
                'phone': phone,
                'email': email,
                'city': city
            }
        )

    def updateUser(username, password, name, phone, email, city):
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
                    'email': email,
                    'city': city
                }
            },
            upsert=True
        )
        print("Updated")
        return True


class Posts:
    """
    {

        "_id": {
            "$oid": ""
        },
        "id": 1,
        "username": "",
        "date": "",
        "price": "",
        "name": "",
        "details": "",

        "type": "",         --> car | land | electronics | part
        "fields": {
            "make": "",
            "model": "",
            "yom": "",
            "mileage": "",
            "transmission": "",
            "fueltype": "",
            "engine": "",
            "options": "",
            "size": ""
            "whatfor": "",
        },
        "images": [
            "",
            ""
        ]

    }
    """

    class Car:
        """
        {
            "id": 1,
            "username": "",
            "date": "",
            "price": "",
            "name": "",
            "details": "",
            "type": "car",
            "fields": {
                "make": "",
                "model": "",
                "yom": "",
                "mileage": "",
                "transmission": "",
                "fueltype": "",
                "engine": "",
                "options": ""
            },
            "images": [
                "",
                ""
            ]
        }
        """
        def getAllPosts():
            temp = []
            for post in posts.find({"type": "car"}):
                temp.append(post)
            return temp

        def getPostsByUsername(username):
            temp = []
            for post in posts.find(
                {
                    "type": "car",
                    "username": username
                }
            ):
                temp.append(post)
            return temp

        def getPostByID(id):
            temp = []
            for post in posts.find(
                {
                    "type": "car",
                    "id": int(id)
                }
            ):
                temp.append(post)
            try:
                return temp[0]
            except:
                return False

        def getPostsByName(name):
            temp = []
            for post in posts.find(
                {
                    "name": {
                        "$regex": f'.*{name}*.',
                        "$options": 'i'  # ignore case
                    },
                    "type": "car"
                }
            ):
                temp.append(post)
            return temp

    class Land:
        """
        {
            "id": 2,
            "username": "",
            "date": "",
            "price": "",
            "name": "",
            "details": "",
            "type": "land",
            "fields": {
                "options": "",
                "size": ""
            },
            "images": [
                "",
                ""
            ]
        }
        """
        def getAllPosts():
            temp = []
            for post in posts.find({"type", "land"}):
                temp.append(post)
            return temp

        def getPostsByUsername(username):
            temp = []
            for post in posts.find(
                {
                    "type": "land",
                    "username": username
                }
            ):
                temp.append(post)
            return temp

        def getPostByID(id):
            temp = []
            for post in posts.find(
                {
                    "type": "land",
                    "id": int(id)
                }
            ):
                temp.append(post)
            try:
                return temp[0]
            except:
                return False

        def getPostsByName(name):
            temp = []
            for post in posts.find(
                {
                    "name": {
                        "$regex": f'.*{name}*.',
                        "$options": 'i'  # ignore case
                    },
                    "type": "land"
                }
            ):
                temp.append(post)
            return temp

    class Electronics:
        """
        {
            "id": 3,
            "username": "",
            "date": "",
            "price": "",
            "name": "",
            "details": "",
            "type": "electronics",
            "fields": {
                "make": "",
                "model": "",
                "options": ""
            },
            "images": [
                "",
                ""
            ]
        }
        """

        def getAllPosts():
            temp = []
            for post in posts.find({"type", "electronics"}):
                temp.append(post)
            return temp

        def getPostsByUsername(username):
            temp = []
            for post in posts.find(
                {
                    "type": "electronics",
                    "username": username
                }
            ):
                temp.append(post)
            return temp

        def getPostByID(id):
            temp = []
            for post in posts.find(
                {
                    "type": "electronics",
                    "id": int(id)
                }
            ):
                temp.append(post)
            try:
                return temp[0]
            except:
                return False
