import typer

from daily import Journal, SqliteJournalDatabase
from daily_cli.env import db_file_path

journal = Journal(SqliteJournalDatabase(db_file_path))

app = typer.Typer()

# Modules in the /commands directory import app and update it with their commands
from .commands import add, delete, edit, view
