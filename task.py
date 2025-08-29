import click
from tracker import commands

@click.group()
def cli():
    """ Task Tracker CLI """
    pass

@cli.command()
@click.argument("description")
def add(description):
    """ Add a new task """
    commands.add_task(description)
    click.echo(f"Task added: {description}")

@cli.command()
def list():
    """ List all the tasks """
    tasks = commands.list_tasks()
    if not tasks:
        click.echo("No tasks found.")
    else:
        for idx, task in enumerate(tasks, 1):
            status = "✔" if task['completed'] else "✘"
            click.echo(f"{idx}. {task['description']} [{status}]")

@cli.command()
@click.argument("task_id", type=int)
def delete(task_id):
    """ Delete a task """
    if commands.delete_task(task_id):
        click.echo(f"Task {task_id} deleted.")
    else:
        click.echo(f"Task {task_id} not found.")

if __name__ == "__main__":
    cli()
