from typing_extensions import Annotated

import typer

from . import app
from daily_journal_cli.db import database


@app.command()
def delete(id: Annotated[int, typer.Argument()]):
    database.delete_entry(id)
