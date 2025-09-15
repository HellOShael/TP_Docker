from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)

MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongo:27017")
DB_NAME   = os.getenv("MONGO_DB", "tpdb")

def get_db():
    client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=2000)
    return client[DB_NAME]

@app.get("/")
def root():
    try:
        db = get_db()
        db.ping.insert_one({"okk": True})
        count = db.ping.count_documents({})
        return f"Mongo = TRUE / Nb docs: {count}"
    except Exception as e:
        return f"Mongo KO: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
