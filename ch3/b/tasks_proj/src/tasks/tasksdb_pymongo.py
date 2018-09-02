from pymongo import MongoClient


def start_tasks_db(db_path: str) -> object:
    return MongoDbCursor(db_path)


class MongoDbCursor(object):
    def __init__(self, db_path: str):
        db_name = db_path.split('/')[-1]
        self.client = MongoClient()
        self.db = self.client['tasks'][f'{db_name}']

    def close(self) -> None:
        self.client.close()

    def get_id(self) -> int:
        if self.count() == 0:
            return 1
        else:
            return self.get_uid()

    def get_uid(self) -> int:
        return self.count() + 1

    def count(self) -> int:
        return self.db.count()

    def insert(self, param: dict):
        self.db.insert_one(param)

    def select(self, ids: int) -> dict:
        return self.db.find_one({'id': ids})

    def delete(self, ids: int):
        self.db.remove({'id': ids})

    def delete_all(self):
        self.db.drop({})
