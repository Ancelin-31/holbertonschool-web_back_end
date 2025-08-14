from pymongo import MongoClient

def list_all(mongo_collection):
    """List all documents in a collection."""
    return list(mongo_collection.find())

if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017/")
    db = client["test_db"]
    collection = db["test_collection"]

    # Insert test data if empty
    if collection.count_documents({}) == 0:
        collection.insert_many([
            {"name": "Alice"},
            {"name": "Bob"},
            {"name": "Charlie"}
        ])

    docs = list_all(collection)
    for doc in docs:
        print(doc)
