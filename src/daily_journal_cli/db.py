import sqlite3
from datetime import date, datetime

cx = sqlite3.connect("daily-journal.db")


class Entry:
    def __init__(self, raw_entry):
        print(raw_entry)
        self.id = raw_entry[0]
        self.content = raw_entry[1]
        self.date = raw_entry[2]
        self.created_at = raw_entry[3]
        self.updated_at = raw_entry[4]


class DB:
    cx = sqlite3.connect("daily-journal.sqlite")

    def __init__(self):
        self.createEntriesTable()

    def createEntriesTable(self):
        """Create Entries table in DB"""
        with cx:
            cu = cx.cursor()
            # cu.execute("DROP TABLE IF EXISTS entries;")
            cu.execute(
                """
                    CREATE TABLE IF NOT EXISTS entries (
                    id INTEGER PRIMARY KEY,
                    content TEXT NOT NULL,
                    date TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                    );
                """
            )

    def get_entries_by_date(self, date: date) -> list[Entry]:
        with cx:
            cu = cx.cursor()
            cu.execute("SELECT * FROM entries WHERE date = ?", (date,))
            rows = cu.fetchall()
        return [Entry(row) for row in rows]

    def get_all_entries(self) -> list[Entry]:
        with cx:
            cu = cx.cursor()
            cu.execute("SELECT * FROM entries;")
            rows = cu.fetchall()
        return [Entry(row) for row in rows]

    def insert_entry(self, content: str, date: date) -> int:
        now = datetime.now()
        row = (content, date, now, now)
        with cx:
            cu = cx.cursor()
            cu.execute(
                "INSERT INTO entries (content, date, created_at, updated_at) VALUES(?, ?, ?, ?);",
                row,
            )
            cu.execute("SELECT last_insert_rowid();")
            rowid = cu.fetchone()
        return rowid


database = DB()


def populate_data():
    now = date.today()
    records = [("test 1", now), ("test 2", now), ("test 3", now)]
    for r in records:
        database.insert_entry(*r)
