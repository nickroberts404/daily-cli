from typing_extensions import Annotated
import typer

from ...daily import Journal, SqliteJournalDatabase
from ..cli_plugin import CLIPlugin

# from . import subcommands
from .subcommands import AddEntryMixin


# Register self in a db that will hold whether it's active or not
class JournalCLI(Journal, CLIPlugin, AddEntryMixin):
    name = "journal"
    app = typer.Typer()

    def _decorator(foo):
        def inner( self ) :
            print "start magic"
            foo( self )
            print "end magic"
        return inner
    def __init__(self, dbFilePath: str):
        db = SqliteJournalDatabase(dbFilePath)
        super().__init__(db)

    # @app.command()
    # def view(
    #     last_n_days: Annotated[int, typer.Option("--last")] = 7,
    #     date_range: Annotated[str, typer.Option("--range", "-r")] = None,
    # ):
    #     return subcommands.view(last_n_days, date_range)

    @app.command()
    def add(
        self,
        date: Annotated[str, typer.Option("--date", "-d")] = None,
        yesterday: Annotated[bool, typer.Option("--yesterday", "-y")] = False,
    ):
        return self.addEntry(date, yesterday)

    # @app.command()
    # def edit(id: Annotated[int, typer.Argument()]):
    #     return subcommands.edit(id)

    # @app.command()
    # def delete(id: Annotated[int, typer.Argument()]):
    #     return subcommands.delete(id)
    
    def registerCommands(self, parentApp: typer.Typer):
        # First we must add all the commmands
        return parentApp.add_typer(self.app, name=self.name)
