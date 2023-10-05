from datetime import date

from .entry import Entry
from .db import JournalDatabase


class Journal:
    def __init__(self, db: JournalDatabase):
        self.db = db

    def get_entry_by_id(self, id: int) -> Entry:
        return self.db.get_entry_by_id(id)

    def get_entries_by_date(self, date: date):
        return self.db.get_entries_by_date(date)

    def get_entries_by_date_range(self, start: date, end: date) -> Entry:
        return self.db.get_entries_by_date_range(start, end)

    def insert_entry(self, content: str, date: date) -> int:
        return self.db.insert_entry(content, date)

    def delete_entry(self, entry_id: int):
        return self.db.delete_entry(entry_id)

    def update_entry_content(self, entry_id: int, content: str):
        return self.db.update_entry_content(entry_id, content)
