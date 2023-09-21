import typer
from rich import print


def main():
    entries = []
    for entry in receive_entries():
        entries.append(entry)
    print("Entries completed: ", len(entries))
    print(entries)


def receive_entries():
    while True:
        input = typer.prompt(
            text="What did you do today?", type=str, default="", show_default=False
        )
        if len(input) == 0:
            break
        else:
            yield input


def run():
    typer.run(main)


if __name__ == "__main__":
    run()
