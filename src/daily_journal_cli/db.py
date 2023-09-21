import sqlite3
from datetime import datetime

cx = sqlite3.connect("daily-journal.db")


def create_tables():
    with cx:
        cu = cx.cursor()
        cu.execute("DROP TABLE IF EXISTS entries;")
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


def get_entries_for_date():
    raise NotImplemented()


def insert_entry(content: str, date: datetime):
    raise NotImplemented()


def test():
    with cx:
        cu = cx.cursor()
        data = cu.execute("SELECT * FROM entries")
        print(data)


def setup():
    create_tables()
    test()
