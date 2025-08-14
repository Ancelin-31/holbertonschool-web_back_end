from mongodb import pymongo


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.
    
    Args:
        mongo_collection: pymongo collection object.
    
    Returns:
        list: A list of all documents in the collection.
              Returns an empty list if there are no documents.
    """
    if mongo_collection is None:
        return []
    
    return list(mongo_collection.find())
