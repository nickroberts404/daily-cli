import typer

app = typer.Typer()

# Modules in the /commands directory import app and update it with their commands
from .commands import new
