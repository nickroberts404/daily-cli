from datetime import date


class Entry:
    def __init__(
        self,
        id: int,
        content: str,
        date: date,
    ):
        self.id = id
        self.content = content
        self.date = date
