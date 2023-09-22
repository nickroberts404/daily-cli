import sqlite3
from datetime import date, datetime

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


def get_entries_for_date(date: date):
    with cx:
        cu = cx.cursor()
        cu.execute("SELECT * FROM entries WHERE date = ?", (date,))
        rows = cu.fetchall()
        print(rows)


def insert_entry(content: str, date: date):
    now = datetime.now()
    with cx:
        cu = cx.cursor()
        row = (content, date, now, now)
        cu.execute(
            "INSERT INTO entries (content, date, created_at, updated_at) VALUES(?, ?, ?, ?)",
            row,
        )


def populate_data():
    now = date.today()
    records = [("test 1", now), ("test 2", now), ("test 3", now)]
    for r in records:
        insert_entry(*r)


def setup():
    create_tables()
