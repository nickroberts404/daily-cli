from abc import ABC, abstractmethod
import typer


class CLIPlugin(ABC):
    name = "plugin"

    @abstractmethod
    def registerCommands(self, parentApp: typer.Typer):
        pass
