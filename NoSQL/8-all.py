import pymongo


def list_all(mongo_collection):
    """ Lists all documents in a MongoDB collection."""
    if mongo_collection is None:
        return []
    
    return list(db.mongo_collection.find())
