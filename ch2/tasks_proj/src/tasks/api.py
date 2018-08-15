import typing
from dataclasses import dataclass


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
    return task.id


def get(task_id: int) -> Task:
    pass


def list_tasks(owenr: typing.Optional[str] = None) -> typing.List:
    pass


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


def stop_tasks_db() -> None:
    pass
