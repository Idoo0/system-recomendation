from dotenv import load_dotenv
import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

load_dotenv()

uri = os.getenv("MONGODB_URI")

try:
    conn = MongoClient(uri)
    print("Database connected successfully")
except ConnectionFailure as e:
    print(f"Error connecting to MongoDB: {e}")
