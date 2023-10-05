import typer
import daily_journal_cli.journal as journal

app = typer.Typer()
app.add_typer(journal.app, name="journal")
app.add_typer(journal.app, name="j")


class Daily:
    def __init__():
        raise NotImplemented


class DailyCLIPlugin:
    name = "plugin"

    def registerCommands(self, parentApp: typer.Typer):
        raise NotImplemented


class DailyCLI(Daily):
    app = typer.Typer()
    plugins = []

    def __init__(super):
        super()

    def registerPlugins(self, plugins: list[DailyCLIPlugin]):
        for p in plugins:
            p.registerCommands(self.app)
        self.plugins = plugins

class SqliteDatabase:
    def __init__(self, dbFilePath):
        self.cx = sqlite3.connect(dbFilePath)
class JournalDatabase():
    def
class JournalDatabaseSqlite(JournalDatabase, SqliteDatabase):

class Journal:
    database = None
    def __init__(database: JournalDatabase):
        
        raise NotImplemented


class JournalCLI(Journal, DailyCLIPlugin):
    name = "journal"
    app = typer.Typer()

    def __init__(super):
        super()
        raise NotImplemented

    def registerCommands(self, parentApp: typer.Typer):
        return parentApp.add_typer(self.app, name=self.name)


class Habit:
    def __init__(dbFilePath):
        raise NotImplemented


class HabitCLI(Habit):
    def __init__(super):
        super()
        raise NotImplemented


