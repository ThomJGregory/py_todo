# Username and password stored as strings in keys.py
from keys import dbUser
from keys import dbPass

from pymongo import MongoClient

# Create the data hierarchy for the main file to pull from
cluster = MongoClient(
    f'mongodb+srv://{dbUser}:{dbPass}@todo-data.aa7rx.mongodb.net/<dbname>?retryWrites=true&w=majority')
db = cluster["todo-list"]
todos = db['todos']
user_data = db['user-data']
