from datetime import date, timedelta

from rich import print
from rich.prompt import Prompt

from daily_cli.util import format_date, string_to_date
from .print_entries import print_entries


def print_prompt(date: date):
    formatted_date = format_date(date)
    print(f":snow_capped_mountain: [bold]What did you do on[/] {formatted_date}?")


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


class InsertEntryMixin:
    def insert_entry(self, date_string: str or None, yesterday: bool):
        target_date = get_target_date(date_string, yesterday)
        existing_entries = self.journal.get_entries_by_date(target_date)
        print_prompt(target_date)
        print_entries(existing_entries)

        for entry in prompt_user_for_entries():
            self.journal.insert_entry(entry, target_date)
