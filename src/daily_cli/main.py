import typer
from daily_cli.cli import journal

app = typer.Typer()
app.add_typer(journal.app, name="journal")


def run():
    app()


if __name__ == "__main__":
    run()
