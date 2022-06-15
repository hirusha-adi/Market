
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
        try:
            return temp[0]
        except:
            return False

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
    class Car:
        """
        {
            "id": 1,
            "username": "",
            "date": "",
            "type": "car",

            "name": "",
            "price": "",
            "details": "",

            "fields": {
                "ctype": "",
                "condition": "",
                "make": "",
                "model": "",
                "yom": "",
                "transmission": "",
                "fueltype": "",
                "engine": "",
                "mileage": "",
                "options": ""
            },
            "images": [
                "http://hirusha.xyz",
                "http://example.com"
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
            "type": "land",

            "name": "",
            "price": "",
            "details": "",

            "fields": {
                "ptype": "",
                "btype": "",
                "size": "",
                "options": ""
            },
            "images": [
                "http://hirusha.xyz",
                "http://example.com"
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
            "type": "electronics",

            "name": "",
            "price": "",
            "details": "",

            "fields": {
                "make": "",
                "model": "",
                "yom": "",
                "power": "",
                "options": ""
            },
            "images": [
                "http://hirusha.xyz",
                "http://example.com"
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

        def getPostsByName(name):
            temp = []
            for post in posts.find(
                {
                    "name": {
                        "$regex": f'.*{name}*.',
                        "$options": 'i'  # ignore case
                    },
                    "type": "electronics"
                }
            ):
                temp.append(post)
            return temp

    class Parts:
        """
        {
            "id": 3,
            "username": "",
            "date": "",
            "type": "electronics",

            "name": "",
            "price": "",
            "details": "",

            "fields": {
                "make": "",
                "model": "",
                "yom": "",
                "whatfor": "",
                "size": "",
                "options": ""
            },
            "images": [
                "http://hirusha.xyz",
                "http://example.com"
            ]

        }
        """

        def getAllPosts():
            temp = []
            for post in posts.find({"type", "parts"}):
                temp.append(post)
            return temp

        def getPostsByUsername(username):
            temp = []
            for post in posts.find(
                {
                    "type": "parts",
                    "username": username
                }
            ):
                temp.append(post)
            return temp

        def getPostByID(id):
            temp = []
            for post in posts.find(
                {
                    "type": "parts",
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
                    "type": "parts"
                }
            ):
                temp.append(post)
            return temp

    def getAllPosts():
        temp = []
        for post in posts.find():
            temp.append(post)
        return temp

    def getPostsByUsername(username):
        temp = []
        for post in posts.find(
            {
                "username": username
            }
        ):
            temp.append(post)
        return temp

    def getPostByID(id):
        temp = []
        for post in posts.find(
            {
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
                }
            }
        ):
            temp.append(post)
        return temp

    def addPost(data):
        posts.insert_one(data)
        