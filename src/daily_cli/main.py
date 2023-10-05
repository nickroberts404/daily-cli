from .cli.daily_cli import DailyCLI
from .cli.journal.journal_cli import setup_journal_plugin

journal_plugin = setup_journal_plugin("daily-journal.sqlite")
cli = DailyCLI()
cli.register_plugins([journal_plugin])


def run():
    cli.run()


if __name__ == "__main__":
    run()
