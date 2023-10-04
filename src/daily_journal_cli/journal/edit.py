from datetime import date
from typing_extensions import Annotated

import typer
from rich.prompt import Prompt

from . import app
from daily_journal_cli.db import database

today = date.today()


@app.command()
def edit(id: Annotated[int, typer.Argument()]):
    entry = database.get_entry_by_id(id)
    edited_content = Prompt.ask("Edit", default=entry.content)
    database.update_entry_content(id, edited_content)
