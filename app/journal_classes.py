from dataclasses import dataclass


@dataclass
class JournalEntry:
    def __init__(self, jid, person_id, text, date_written, author, text_keyword, location):
        self.jid = jid
        self.person_id = person_id
        self.text = text
        self.date_written = date_written
        self.author = author
        self.text_keyword = text_keyword
        self.location = location


class Journal:
    def __init__(self):
        self.journal_entries = []

    def add_entry(self, entry):
        self.journal_entries.append(entry)

