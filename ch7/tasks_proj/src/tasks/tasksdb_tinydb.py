from tinydb import TinyDB, Query


def start_tasks_db(db_path):
    return TinyDbCursor(db_path)


class TinyDbCursor(object):
    def __init__(self, db_path):
        self.db = TinyDB(f'{db_path}/db.json')

    def close(self) -> None:
        self.db.close()

    def get_id(self) -> int:
        if not self.db.all():
            return 1
        else:
            return self.get_uid()

    def get_uid(self) -> int:
        return self.count() + 1

    def get_all_list(self) -> list:
        return self.db.all()

    def get_list(self, owner) -> list:
        return self.db.search(Query().owner == owner)

    def count(self) -> int:
        return len(self.db)

    def insert(self, param: dict) -> None:
        self.db.insert(param)

    def select(self, ids: int) -> dict:
        return self.db.search(Query().id == ids)[0]

    def delete(self, ids: int) -> None:
        self.db.remove(Query().id == ids)

    def delete_all(self):
        self.db.purge()
