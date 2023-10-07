from abc import ABC, abstractmethod
from datetime import date, datetime

import sqlite3


# Abstract
class SqliteDatabase(ABC):
    def __init__(self, dbFilePath):
        self.cx = sqlite3.connect(dbFilePath)
        self.createTables()

    @abstractmethod
    def createTables(self):
        pass


def sqlite_date_to_date(db_date: str) -> date:
    return datetime.strptime(db_date, "%Y-%m-%d").date()
