from typing_extensions import Annotated

import typer
from ..journal_cli import app, journal


@app.command()
def delete(id: Annotated[int, typer.Argument()]):
    return journal.delete_entry(id)
