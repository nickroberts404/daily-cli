from abc import ABC, abstractmethod

from datetime import date


# Add comments
class HabitsDatabase(ABC):
    @abstractmethod
    def get_all_habits(self):
        pass
