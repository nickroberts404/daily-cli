from rich.prompt import Prompt


class EditEntryMixin:
    def edit_entry(self, id: int):
        entry = self.journal.get_entry_by_id(id)
        edited_content = Prompt.ask("Edit", default=entry.content)
        self.journal.update_entry_content(id, edited_content)
