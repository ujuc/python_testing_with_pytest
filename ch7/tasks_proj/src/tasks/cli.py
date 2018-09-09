from contextlib import contextmanager

import click
import tasks


@click.group()
@click.version_option(version='0.1.1')
def tasks_cli():
    """Run the tasks application."""
    pass


@tasks_cli.command(name='list', help='list tasks')
@click.option('-o', '-owner', default=None,
              help='list tasks with this owner')
def list_tasks(owner):
    """
    List tasks in db.

    If owner given, only list tasks with that owner.

    :param owner:
    :return:
    """
    formatstr = '{: >4} {: >10} {: >5} {}'
    print(formatstr.format('ID', 'owner', 'done', 'summary'))
    print(formatstr.format('--', '-----', '----', '-------'))
    with _tasks_db():
        for t in tasks.list_tasks(owner):
            done = 'True' if t.done else 'False'
            owner = '' if t.owner is None else t.owner
            print(formatstr.format(
                t.id, owner, done, t.summary
            ))


@contextmanager
def _tasks_db():
    config = tasks.config.get_config()
    tasks.start_tasks_db(config.db_path, config.db_type)
    yield
    tasks.stop_tasks_db()


if __name__ == '__main__':
    tasks_cli()

