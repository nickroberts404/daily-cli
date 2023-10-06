import typer
import daily_cli.cli.journal as journal

app = typer.Typer()
app.add_typer(journal.app, name="journal")


def run():
    app()


if __name__ == "__main__":
    run()
