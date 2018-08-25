from pymongo import MongoClient

_collection = object


def start_tasks_db(db_path: str) -> object:
    client = MongoClient()

    global _collection
    db = client['local'][f'{db_path}']
    _collection = db.tasks
    return _collection


def ids():
    global _collection
    if _collection.count() == 0:
        return 1
    else:
        return _collection.count() + 1


def count() -> int:
    global _collection
    return _collection.count()

