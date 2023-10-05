class DeleteEntryMixin:
    def delete_entry(self, id: int):
        self.journal.delete_entry(id)
