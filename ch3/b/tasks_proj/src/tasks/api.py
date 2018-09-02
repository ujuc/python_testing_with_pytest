import typing
from dataclasses import dataclass

from tinydb import TinyDB, where, Query


_tasksdb = object


@dataclass
class Task:
    summary: str = None
    owner: str = None
    done: bool = False
    id: int = None

    def _asdict(self):
        return {
            'summary': self.summary,
            'owner': self.owner,
            'done': self.done,
            'id': self.id
        }

    def _replace(self, *args, **kwargs):
        self.summary = kwargs['summary'] \
            if kwargs.get('summary') else self.summary
        self.owner = kwargs['owner'] if kwargs.get('owner') else self.owner
        self.done = kwargs['done'] if kwargs.get('done') else self.done
        self.id = kwargs['id'] if kwargs.get('id') else self.id

        return self


def add(task: Task) -> int:
    if not isinstance(task, Task):
        raise TypeError

    global _tasksdb
    task.id = _tasksdb.get_uid()
    _tasksdb.insert(task._asdict())
    return task.id


def get(task_id: int) -> Task:
    if not isinstance(task_id, int):
        raise TypeError

    global _tasksdb
    task_db = _tasksdb.select(task_id)
    task = Task(
        task_db['summary'], task_db['owner'], task_db['done'], task_db['id']
    )
    return task


def list_tasks(owner: typing.Optional[str] = None) -> typing.List:
    if not isinstance(owner, str):
        raise TypeError

    return []


def count() -> int:
    global _tasksdb
    return _tasksdb.count()


def update(task_id: int, task: Task) -> None:
    if not isinstance(task_id, int) or not isinstance(task, Task):
        raise TypeError


def delete(task_id: int) -> None:
    global _tasksdb
    _tasksdb.delete(task_id)


def delete_all() -> None:
    global _tasksdb
    _tasksdb.delete_all()


def unique_id() -> int:
    global _tasksdb
    uid = _tasksdb.get_uid()
    return uid


def start_tasks_db(db_path: str, db_type: str) -> None:
    """Connect API functions to a db."""
    if not isinstance(db_path, str):
        raise TypeError('db_path must be a string')

    global _tasksdb

    if db_type == 'tiny':
        from . import tasksdb_tinydb
        _tasksdb = tasksdb_tinydb.start_tasks_db(db_path)
    elif db_type == 'mongo':
        from . import tasksdb_pymongo
        _tasksdb = tasksdb_pymongo.start_tasks_db(db_path)
    else:
        raise ValueError("db_type must be a 'tiny' or 'mongo'")


def stop_tasks_db() -> None:
    global _tasksdb
    _tasksdb.close()
