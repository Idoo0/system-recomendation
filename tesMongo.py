from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://uniq-sysrec-db:DSxMKc0cK9DuNSDV@uniq-cluster.c6vot.mongodb.net/?retryWrites=true&w=majority&appName=uniq-cluster"
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.uniq
coll = db.transaction
