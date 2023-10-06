from typing_extensions import Annotated

import typer
from rich.prompt import Prompt
from ..journal_cli import app, journal


@app.command()
def edit(id: Annotated[int, typer.Argument()]):
    entry = journal.get_entry_by_id(id)
    edited_content = Prompt.ask("Edit", default=entry.content)
    journal.update_entry_content(id, edited_content)
