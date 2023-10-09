from typing_extensions import Annotated
from datetime import date, timedelta

import typer
from rich import print
from rich.prompt import Prompt

from ..journal_cli import app, journal
from daily_cli.util import format_date, string_to_date
from .print_entries import print_entries


def print_prompt(date: date):
    formatted_date = format_date(date)
    isToday = date == date.today()
    isYesterday = date == date.today() - timedelta(days=1)
    message = f":snow_capped_mountain: [bold]What did you do "
    if isToday:
        message += "today"
    elif isYesterday:
        message += "yesterday"
    else:
        message += "on"
    message += f"[/] {formatted_date}?"
    print(message)


def get_target_date(date_string: str or None, yesterday: bool) -> date:
    target_date = date.today()
    if yesterday:
        target_date -= timedelta(days=1)
    if date_string:
        target_date = string_to_date(date_string)
    return target_date


def prompt_user_for_entries():
    while True:
        input = Prompt.ask("")
        if len(input) == 0:
            break
        else:
            yield input


def print_existing_entries(date: date):
    existing_entries = journal.get_entries_by_date(date)
    print_entries(existing_entries)


def collect_entries(date: date):
    for entry in prompt_user_for_entries():
        journal.insert_entry(entry, date)


@app.command()
def add(
    date: Annotated[str, typer.Option("--date", "-d")] = None,
    yesterday: Annotated[bool, typer.Option("--yesterday", "-y")] = False,
):
    target_date = get_target_date(date, yesterday)

    print_prompt(target_date)
    print_existing_entries(target_date)
    collect_entries(target_date)


# @app.callback(invoke_without_command=True)
# def add(ctx):
#     print(cls)
#     if cls.subcommand_called:
#         pass
#     else:
#         add()
