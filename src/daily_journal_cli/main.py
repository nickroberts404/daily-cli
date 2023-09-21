import typer
import datetime
from rich import print
from rich.prompt import Prompt
from typing_extensions import Annotated

existing_entries = ["Ate breakfast", "Went on a run with Lauren"]
today = datetime.date.today()


def format_date(date):
    return date.strftime("%b %d, %Y")


def get_target_date(date):
    target_date = today
    if date:
        try:
            target_date = datetime.datetime.strptime(date, "%m/%d/%Y")
        except:
            print(
                "[red bold]Please provide date in valid format[/] (example: 05/26/1994)."
            )
            raise typer.Exit()
    return target_date


def collect_entries(date):
    formatted_date = format_date(date)
    entries = []
    print(
        f"[bold blue]What did you do today [not bold italic]({formatted_date})[/]?[/]"
    )
    for entry in existing_entries:
        print(f"[bold blue]*[/] {entry}")
    for entry in receive_entries():
        entries.append(entry)
        # TODO Add entries to DB


def receive_entries():
    while True:
        input = Prompt.ask("")
        if len(input) == 0:
            break
        else:
            yield input


def main(date: Annotated[str, typer.Option("--date", "-d")] = None):
    target_date = get_target_date(date)
    collect_entries(target_date)


def run():
    typer.run(main)


if __name__ == "__main__":
    run()
