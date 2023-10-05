from daily_journal_cli.db import database


def delete(id: int):
    database.delete_entry(id)
