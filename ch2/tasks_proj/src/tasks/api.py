import typing
from dataclasses import dataclass

from tinydb import TinyDB, Query

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

    return task.id


def get(task_id: int) -> Task:
    if not isinstance(task_id, int):
        raise TypeError

    return Task


def list_tasks(owner: typing.Optional[str] = None) -> typing.List:
    if not isinstance(owner, str):
        raise TypeError

    return []


def count() -> int:
    pass


def update(taks_id: int, task: Task) -> None:
    pass


def delete(task_id: int) -> None:
    pass


def delete_all() -> None:
    pass


def unique_id() -> int:
    pass


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
