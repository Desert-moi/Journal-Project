import db.mysql_repository
from app.journal_classes import *


class Services:
    def __init__(self):
        self.repo = db.mysql_repository.MysqlRepository()
        self.journals = self.repo.load_journals()

    # Use case 1: Call journals based on an author
    def recall_author(self, target_author: str):
        """Calls the journal entries of target_author; should they exist in the database"""

        # Filter entries by the target author
        filtered_entries = [entry for entry in self.journals if entry.get_author() == target_author.lower]

        # Print the filtered entries
        if filtered_entries:
            return filtered_entries

    #Use case 2: Recall journals based on keywords

