from tinydb import TinyDB, Query

_db = object


def start_tasks_db(db_path):
    global _db
    _db =  TinyDB(f'{db_path}/db.json')
    return _db


def ids():
    global _db
    if not _db.all():
        return 1
    else:
        return _db.all()[-1].doc_id + 1


def count() -> int:
    global _db
    return len(_db)


def uid() -> int:
    global _db
    uid = _db.all()[-1].doc_id + 1
    return uid
