import requests
import os
from config.db import conn
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

db = conn["product_recommendation"]
collection = db["crm"]


def updateTransactionData():

    #   current_time = datetime.utcnow()
    #   lastUpdate = int(current_time.timestamp() * 1000)
    lastUpdate = 1705363200000
    api_url = os.getenv("API_URL") + str(lastUpdate)
    headers = {
        "Authorization": os.getenv("API_AUTH")
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        delete_result = collection.delete_many({})
        print(
            f"Deleted {delete_result.deleted_count} existing records from MongoDB.")

        response_data = response.json()
        data = response_data.get("data", [])

        if isinstance(data, list) and data:
            collection.insert_many(data)
            print(f"Inserted {len(data)} new records into MongoDB!")
        else:
            print("No valid data found to insert.")

        return {"lastUpdate": lastUpdate, "message": "Data updated successfully!"}
    else:
        print(f"Failed to fetch data from API. Status Code: {
              response.status_code}")
        print(response.text)
        return {"error": "Failed to fetch data", "status_code": response.status_code}
