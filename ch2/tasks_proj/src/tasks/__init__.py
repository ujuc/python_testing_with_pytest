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
        self.summary = kwargs['summary'] if kwargs.get('summary') else self.summary
        self.owner = kwargs['owner'] if kwargs.get('owner') else self.owner
        self.done = kwargs['done'] if kwargs.get('done') else self.done
        self.id = kwargs['id'] if kwargs.get('id') else self.id

        return self
