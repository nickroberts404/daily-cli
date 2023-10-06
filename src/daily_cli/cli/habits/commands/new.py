from typing_extensions import Annotated

import typer
from rich import print
from rich.prompt import Prompt

from ..habits_cli import app


@app.command()
def new():
    print("Adding new habit!")
