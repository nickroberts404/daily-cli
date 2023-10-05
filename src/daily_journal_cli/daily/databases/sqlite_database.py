from abc import ABC, abstractmethod

import sqlite3


# Abstract
class SqliteDatabase(ABC):
    def __init__(self, dbFilePath):
        self.cx = sqlite3.connect(dbFilePath)
        self.createTables()

    @abstractmethod
    def createTables(self):
        pass
