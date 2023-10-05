from rich import print
from daily_journal_cli.db import Entry


def print_entries(entries: list[Entry]):
    for entry in entries:
        print(f"[bold blue]*[/] {entry.content} [dim]({entry.id})[/]")
