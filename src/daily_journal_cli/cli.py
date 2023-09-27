import typer
import daily_journal_cli.journal.journal as journal

app = typer.Typer()
app.add_typer(journal.app, name="journal")
app.add_typer(journal.app, name="j")
