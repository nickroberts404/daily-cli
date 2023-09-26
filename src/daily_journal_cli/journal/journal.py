from datetime import datetime, date, timedelta
from typing_extensions import Annotated

import typer
from rich import print
from rich.prompt import Prompt

from daily_journal_cli.db import DB, Entry
from daily_journal_cli.cli import app

database = DB()
today = date.today()


def format_date(date: date) -> str:
    return date.strftime("%b %d, %Y")


def string_to_date(date_string: str) -> date:
    return datetime.strptime(date_string, "%m/%d/%Y").date()


def get_target_date(date_string: str or None, yesterday: bool) -> date:
    target_date = today
    if yesterday:
        target_date -= timedelta(days=1)
    if date_string:
        try:
            target_date = string_to_date(date_string)
        except:
            print(
                "[red bold]Please provide date in valid format[/] (example: 05/26/1994)."
            )
            raise typer.Exit()
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
def journal(
    date: Annotated[str, typer.Option("--date", "-d")] = None,
    yesterday: Annotated[bool, typer.Option("--yesterday", "-y")] = False,
):
    target_date = get_target_date(date, yesterday)
    collect_entries(target_date)


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    date: Annotated[str, typer.Option("--date", "-d")] = None,
    yesterday: Annotated[bool, typer.Option("--yesterday", "-y")] = False,
):
    if ctx.invoked_subcommand is not None:
        return
    journal(date=date, yesterday=yesterday)
