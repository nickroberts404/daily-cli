from datetime import date, datetime


class Entry:
    def __init__(
        self,
        id: int,
        content: str,
        date: date,
        created_at: datetime,
        updated_at: datetime,
    ):
        self.id = id
        self.content = content
        self.date = date
        self.created_at = created_at
        self.updated_at = updated_at
