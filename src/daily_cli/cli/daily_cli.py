import typer
from .cli_plugin import CLIPlugin


class DailyCLI:
    app = typer.Typer()
    plugins = []

    def register_plugins(self, plugins: list[CLIPlugin]):
        for p in plugins:
            p.register_commands(self.app)
        self.plugins = plugins

    def run(self):
        self.app()
