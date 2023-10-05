import typer
from .cli_plugin import CLIPlugin


class DailyCLI:
    app = typer.Typer()
    plugins = []

    def registerPlugins(self, plugins: list[CLIPlugin]):
        for p in plugins:
            p.registerCommands(self.app)
        self.plugins = plugins

    def run(self):
        self.app()
