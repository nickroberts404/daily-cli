import typer
from daily_cli.cli import journal, habits

app = typer.Typer()
app.add_typer(journal.app, name="journal")
app.add_typer(habits.app, name="habits")


def run():
    app()


if __name__ == "__main__":
    run()
