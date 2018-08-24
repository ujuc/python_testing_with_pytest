from tinydb import TinyDB, Query


def start_tasks_db(db_path):
    return TinyDB(f'{db_path}/db.json')
