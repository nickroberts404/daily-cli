from abc import ABC, abstractmethod
import typer


class CLIPlugin(ABC):
    name = "plugin"

    @abstractmethod
    def register_commands(self, parentApp: typer.Typer):
        pass
