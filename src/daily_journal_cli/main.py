from .cli.daily_cli import DailyCLI
from .cli.journal.journal_cli import JournalCLI

journal_plugin = JournalCLI("daily-journal.sqlite")
cli = DailyCLI()
cli.registerPlugins([journal_plugin])


def run():
    cli.run()


if __name__ == "__main__":
    run()
