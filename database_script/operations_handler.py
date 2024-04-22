from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from constants import Constants
from dotenv import dotenv_values

uri = "mongodb://localhost:27017"
client = MongoClient(uri, server_api=ServerApi("1"))
db = client.test

def addErrorHandling(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(Constants.error_message.format(e))
    return wrapper

@addErrorHandling
def read(db, name=None):
    print(Constants.read_operation)
    params = {"name": name} if name else {}
    return list(db.cats.find(params)) if len(db.cats.find(params)) == 0 else print(Constants.not_found.format(name))


def create(db, name, age, features):
    print(Constants.create_operation)
    return db.cats.insert_one({"name": name, "age": age, "features": features})


def create_banch_of_records():
    db.cats.insert_many(
        [
            {
                "name": "Luna",
                "age": 2,
                "features": ["small", "gray", "loves milk", "likes to cuddle"],
            },
            {
                "name": "Mittens",
                "age": 4,
                "features": ["big", "white", "loves meow", "playful"],
            },
            {
                "name": "Oreo",
                "age": 3,
                "features": ["small", "black", "loves milk", "laid back"],
            },
            {
                "name": "Patches",
                "age": 6,
                "features": ["big", "gray", "loves meow", "energetic"],
            },
            {
                "name": "Snowball",
                "age": 1,
                "features": ["small", "white", "loves meow", "cuddly"],
            },
        ]
    )



def update(db, name, age=None, features=None):
    print(Constants.update_operation)

    if features is None and age is not None:
        return db.cats.update_one({"name": name}, {"$set": {"age": age}}, upsert=False)

    if features is not None:
        update_params = {"$addToSet": {"features": {"$each": features}}}
        if age is not None:
            update_params["$set"] = {"age": age}
        return db.cats.update_one({"name": name}, update_params, upsert=False)

    return None


def delete(db, name=None):
    print(Constants.delete_operation)
    if name:
        return db.cats.delete_one({"name": name})
    return db.cats.delete_many({})


def print_all_results(records):
    print(Constants.records_info)
    for record in records:
        print(
            f"{record['_id']}: {record['name']}, {record['age']}, {record['features']}"
        )
