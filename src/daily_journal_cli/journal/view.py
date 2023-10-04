from typing_extensions import Annotated
from collections import defaultdict
from datetime import date, timedelta

import typer
from rich import print

from . import app
from daily_journal_cli.db import database
from daily_journal_cli.util import format_date, string_to_date
from .print_entries import print_entries

today = date.today()


def split_date_range(date_range: str) -> list[date]:
    dates = date_range.split("-")
    if len(dates) != 2:
        print(
            "[red bold]Please provide date range in valid format[/] (example: 05/26/1994-06/01/1994)."
        )
        raise typer.Exit()
    return [string_to_date(d) for d in dates]


def date_range_by_days_ago(days: int) -> list[date]:
    start_date = today - timedelta(days=days - 1)
    return [start_date, today]


@app.command()
def view(
    last_n_days: Annotated[int, typer.Option("--last")] = 7,
    date_range: Annotated[str, typer.Option("--range", "-r")] = None,
):
    if date_range:
        start, end = split_date_range(date_range)
    else:
        start, end = date_range_by_days_ago(last_n_days)
    existing_entries = database.get_entries_by_date_range(start, end)
    # Group existing_entries by date
    entries_grouped_by_date = defaultdict(list)
    for entry in existing_entries:
        entries_grouped_by_date[entry.date].append(entry)

    difference_in_days = (end - start).days + 1
    all_dates = [start + timedelta(days=x) for x in range(difference_in_days)]

    for d in all_dates:
        print(format_date(d))
        entries = entries_grouped_by_date[d]
        if len(entries) > 0:
            print_entries(entries)
        else:
            print("[red]No entries[/]")
        print("")  # Would be cool to print a "rule" here, if we switch to rich.console
