import typing
from dataclasses import dataclass
import random

from tinydb import TinyDB, where, Query

db = object

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

    global db
    if not db.all():
        task.id = 1
    else:
        task.id = db.all()[-1].doc_id + 1

    db.insert(task._asdict())
    return task.id


def get(task_id: int) -> Task:
    if not isinstance(task_id, int):
        raise TypeError

    global db
    task_db = db.search(Query().id == task_id)[0]
    task = Task(
        task_db['summary'], task_db['owner'], task_db['done'], task_db['id']
    )
    return task


def list_tasks(owner: typing.Optional[str] = None) -> typing.List:
    if not isinstance(owner, str):
        raise TypeError

    return []


def count() -> int:
    pass


def update(task_id: int, task: Task) -> None:
    if not isinstance(task_id, int) or not isinstance(task, Task):
        raise TypeError


def delete(task_id: int) -> None:
    pass


def delete_all() -> None:
    pass


def unique_id() -> int:
    global db
    uid = db.all()[-1].doc_id + 1
    return uid


def start_tasks_db(db_path: str, db_type: str) -> None:
    if db_type not in ('tiny', 'mongo'):
        raise ValueError("db_type must be a 'tiny' or 'mongo'")

    if db_type == 'tiny':
        global db
        db = TinyDB(f'{db_path}/db.json')
    elif db_type == 'mongo':
        pass


def stop_tasks_db() -> None:
    global db
    db.close()
