import sqlite3
from datetime import date, datetime


def db_date_to_date(db_date: str) -> date:
    return datetime.strptime(db_date, "%Y-%m-%d").date()


class Entry:
    def __init__(self, raw_entry):
        self.id = raw_entry[0]
        self.content = raw_entry[1]
        self.date = db_date_to_date(raw_entry[2])
        self.created_at = raw_entry[3]
        self.updated_at = raw_entry[4]


class DB:
    cx = sqlite3.connect("daily-journal.sqlite")

    def __init__(self):
        self.createEntriesTable()

    def createEntriesTable(self):
        """Create Entries table in DB"""
        with self.cx:
            cu = self.cx.cursor()
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
        with self.cx:
            cu = self.cx.cursor()
            cu.execute("SELECT * FROM entries WHERE date = ?", (date,))
            rows = cu.fetchall()
        return [Entry(row) for row in rows]

    def get_entries_by_date_range(self, start: date, end: date) -> list[Entry]:
        with self.cx:
            cu = self.cx.cursor()
            cu.execute(
                "SELECT * FROM entries WHERE date >= ? AND date <= ?", (start, end)
            )
            rows = cu.fetchall()
        return [Entry(row) for row in rows]

    def get_all_entries(self) -> list[Entry]:
        with self.cx:
            cu = self.cx.cursor()
            cu.execute("SELECT * FROM entries;")
            rows = cu.fetchall()
        return [Entry(row) for row in rows]

    def get_entry_by_id(self, id: int) -> Entry or None:
        with self.cx:
            cu = self.cx.cursor()
            cu.execute("SELECT * FROM entries where id = ?;", (id,))
            row = cu.fetchone()
        return Entry(row)

    def insert_entry(self, content: str, date: date) -> int:
        now = datetime.now()
        row = (content, date, now, now)
        with self.cx:
            cu = self.cx.cursor()
            cu.execute(
                "INSERT INTO entries (content, date, created_at, updated_at) VALUES(?, ?, ?, ?);",
                row,
            )
            cu.execute("SELECT last_insert_rowid();")
            rowid = cu.fetchone()
        return rowid

    def update_entry_content(self, id: int, content: str):
        now = datetime.now()
        with self.cx:
            cu = self.cx.cursor()
            cu.execute(
                "UPDATE entries SET content = ?, updated_at = ? WHERE id = ?;",
                (content, now, id),
            )

    def delete_entry(self, id: int):
        with self.cx:
            cu = self.cx.cursor()
            cu.execute(
                "DELETE FROM entries WHERE id = ?;",
                (id,),
            )


database = DB()
