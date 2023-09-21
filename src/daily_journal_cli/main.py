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


def print_collect_entries_header(date):
    formatted_date = format_date(date)
    print(
        f"[bold blue]What did you do today [not bold italic]({formatted_date})[/]?[/]"
    )


def print_entry_list(entries):
    for entry in entries:
        print(f"[bold blue]*[/] {entry}")


def prompt_user_for_entries():
    while True:
        input = Prompt.ask("")
        if len(input) == 0:
            break
        else:
            yield input


def collect_entries(date):
    entries = []
    print_collect_entries_header(date)
    print_entry_list(existing_entries)
    for entry in prompt_user_for_entries():
        entries.append(entry)
        # TODO Add entries to DB


def main(date: Annotated[str, typer.Option("--date", "-d")] = None):
    target_date = get_target_date(date)
    collect_entries(target_date)


def run():
    typer.run(main)


if __name__ == "__main__":
    run()
