from datetime import date

from rich.prompt import Prompt

from daily_journal_cli.db import database

today = date.today()


def edit(id: int):
    entry = database.get_entry_by_id(id)
    edited_content = Prompt.ask("Edit", default=entry.content)
    database.update_entry_content(id, edited_content)
