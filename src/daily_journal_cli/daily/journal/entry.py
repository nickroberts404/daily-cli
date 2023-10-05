from datetime import date, datetime


def db_date_to_date(db_date: str) -> date:
    return datetime.strptime(db_date, "%Y-%m-%d").date()


# divorce this from its marriage with sqlite
class Entry:
    def __init__(self, raw_entry):
        self.id = raw_entry[0]
        self.content = raw_entry[1]
        self.date = db_date_to_date(raw_entry[2])
        self.created_at = raw_entry[3]
        self.updated_at = raw_entry[4]
