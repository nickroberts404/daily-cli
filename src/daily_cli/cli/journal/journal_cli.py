from typing_extensions import Annotated
import typer

from daily import Journal, SqliteJournalDatabase
from ..cli_plugin import CLIPlugin

# from . import subcommands
from .mixins import (
    InsertEntryMixin,
    DeleteEntryMixin,
    EditEntryMixin,
    ViewEntriesMixin,
)


# Register self in a db that will hold whether it's active or not
class JournalCLI(
    CLIPlugin, InsertEntryMixin, DeleteEntryMixin, EditEntryMixin, ViewEntriesMixin
):
    name = "journal"
    app = typer.Typer()

    def __init__(self, dbFilePath: str):
        db = SqliteJournalDatabase(dbFilePath)
        self.journal = Journal(db)

    def register_commands(self, parentApp: typer.Typer):
        # First we must add all the commmands
        return parentApp.add_typer(self.app, name=self.name)


def setup_journal_plugin(dbFilePath: str) -> JournalCLI:
    journal_cli = JournalCLI(dbFilePath)
    journal_app = journal_cli.app

    @journal_app.command()
    def add(
        date: Annotated[str, typer.Option("--date", "-d")] = None,
        yesterday: Annotated[bool, typer.Option("--yesterday", "-y")] = False,
    ):
        return journal_cli.insert_entry(date, yesterday)

    @journal_app.command()
    def view(
        last_n_days: Annotated[int, typer.Option("--last")] = 7,
        date_range: Annotated[str, typer.Option("--range", "-r")] = None,
    ):
        return journal_cli.view_entries(last_n_days, date_range)

    @journal_app.command()
    def edit(id: Annotated[int, typer.Argument()]):
        return journal_cli.edit_entry(id)

    @journal_app.command()
    def delete(id: Annotated[int, typer.Argument()]):
        return journal_cli.delete_entry(id)

    return journal_cli
