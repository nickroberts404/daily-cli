from datetime import datetime, date, timedelta
from typing_extensions import Annotated

import typer
from rich import print
from rich.prompt import Prompt

from daily_journal_cli.db import DB, Entry

database = DB()
today = date.today()

app = typer.Typer()


def format_date(date: date) -> str:
    return date.strftime("%b %d, %Y")


def string_to_date(date_string: str) -> date:
    try:
        return datetime.strptime(date_string, "%m/%d/%Y").date()
    except:
        print("[red bold]Please provide date in valid format[/] (example: 05/26/1994).")
        raise typer.Exit()


def get_target_date(date_string: str or None, yesterday: bool) -> date:
    target_date = today
    if yesterday:
        target_date -= timedelta(days=1)
    if date_string:
        target_date = string_to_date(date_string)
    return target_date


def print_collect_entries_header(date: date):
    formatted_date = format_date(date)
    print(
        f"[bold blue]What did you do today [not bold italic]({formatted_date})[/]?[/]"
    )


def print_entry_list(entries: list[Entry]):
    for entry in entries:
        print(f"[bold blue]*[/] {entry.content} [dim]({entry.id})[/]")


def prompt_user_for_entries():
    while True:
        input = Prompt.ask("")
        if len(input) == 0:
            break
        else:
            yield input


def collect_entries(date: date):
    existing_entries = database.get_entries_by_date(date)
    print_collect_entries_header(date)
    print_entry_list(existing_entries)
    for entry in prompt_user_for_entries():
        database.insert_entry(entry, date)


@app.command()
def view(
    date_range: Annotated[str, typer.Option("--range", "-r")] = None,
    last_n_days: Annotated[int, typer.Option("--last")] = 7,
):
    print("Not yet implemented")


@app.command()
def edit(id: Annotated[int, typer.Argument()]):
    entry = database.get_entry_by_id(id)
    edited_content = Prompt.ask("Edit", default=entry.content)
    database.update_entry_content(id, edited_content)


@app.command()
def delete(id: Annotated[int, typer.Argument()]):
    database.delete_entry(id)


DateOption = Annotated[str, typer.Option("--date", "-d")]
YesterdayOption = Annotated[bool, typer.Option("--yesterday", "-y")]


@app.command()
def add(
    date: DateOption = None,
    yesterday: YesterdayOption = False,
):
    target_date = get_target_date(date, yesterday)
    collect_entries(target_date)


@app.callback(invoke_without_command=True)
def default(
    ctx: typer.Context,
    date: DateOption = None,
    yesterday: YesterdayOption = False,
):
    if ctx.invoked_subcommand is not None:
        return
    add(date=date, yesterday=yesterday)
