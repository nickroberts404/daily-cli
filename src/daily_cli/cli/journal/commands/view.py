from typing_extensions import Annotated
from collections import defaultdict
from datetime import date, timedelta

import typer
from rich import print

from ..journal_cli import app, journal
from daily_cli.util import format_date, string_to_date
from .print_entries import print_entries


def split_date_range(date_range: str) -> list[date]:
    dates = date_range.split("-")
    if len(dates) != 2:
        print(
            "[red bold]Please provide date range in valid format[/] (example: 05/26/1994-06/01/1994)."
        )
        raise typer.Exit()
    return [string_to_date(d) for d in dates]


def date_range_by_days_ago(days: int) -> list[date]:
    today = date.today()
    start_date = today - timedelta(days=days - 1)
    return [start_date, today]


def get_range(date_range: str, last_n_days: int) -> list[date]:
    if date_range:
        start, end = split_date_range(date_range)
    else:
        start, end = date_range_by_days_ago(last_n_days)
    return [start, end]


def group_entries_by_date(entries):
    entries_grouped_by_date = defaultdict(list)
    for e in entries:
        entries_grouped_by_date[e.date].append(e)
    return entries_grouped_by_date


def get_list_of_dates(start: date, end: date) -> list[date]:
    difference_in_days = (end - start).days + 1
    return [start + timedelta(days=x) for x in range(difference_in_days)]


def print_entries_by_date(entries_grouped_by_date, list_of_dates):
    for d in list_of_dates:
        print(format_date(d))
        entries = entries_grouped_by_date[d]
        if len(entries) > 0:
            print_entries(entries)
        else:
            print("[red]No entries[/]")
        print("")  # Would be cool to print a "rule" here, if we switch to rich.console


@app.command()
def view(
    last_n_days: Annotated[int, typer.Option("--last")] = 7,
    date_range: Annotated[str, typer.Option("--range", "-r")] = None,
):
    start, end = get_range(date_range, last_n_days)
    existing_entries = journal.get_entries_by_date_range(start, end)
    entries_grouped_by_date = group_entries_by_date(existing_entries)
    list_of_dates = get_list_of_dates(start, end)
    print_entries_by_date(entries_grouped_by_date, list_of_dates)
