from abc import ABC, abstractmethod

from ..entry import Entry
from datetime import date


# Add comments
class JournalDatabase(ABC):
    @abstractmethod
    def get_entries_by_date(self, date: date) -> list[Entry]:
        pass

    @abstractmethod
    def get_entries_by_date_range(self, start: date, end: date) -> list[Entry]:
        pass

    @abstractmethod
    def get_all_entries(self) -> list[Entry]:
        pass

    @abstractmethod
    def get_entry_by_id(self, id: int) -> Entry or None:
        pass

    @abstractmethod
    def insert_entry(self, content: str, date: date) -> int:
        pass

    @abstractmethod
    def update_entry_content(self, id: int, content: str):
        pass

    @abstractmethod
    def delete_entry(self, id: int):
        pass
