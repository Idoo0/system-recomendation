import pandas as pd
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# MongoDB connection setup
uri = "mongodb+srv://uniq-sysrec-db:DSxMKc0cK9DuNSDV@uniq-cluster.c6vot.mongodb.net/?retryWrites=true&w=majority&appName=uniq-cluster"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.uniq
coll = db.transaction

# Read CSV file
csv_file_path = 'member_transaction.csv'
df = pd.read_csv(csv_file_path)

# Convert dataframe records to dictionaries
records = df.to_dict(orient='records')

# Insert the data into MongoDB collection
try:
    coll.insert_many(records)
    print("Data successfully inserted into MongoDB!")
except Exception as e:
    print(f"An error occurred: {e}")
