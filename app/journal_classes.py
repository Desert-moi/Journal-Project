from dataclasses import dataclass


class JournalEntry:
    def __init__(self, jid, text, date_written, author, text_keyword, location):
        self.id = jid
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


@dataclass(frozen=True)
class Token:
    term: str


class TermDocumentIndex:
    def __init__(self):
        self.vocabulary = set()
        self.postings = {}

    def add_to_vocabulary(self, token):
        self.vocabulary.add(token)

    def add_posting(self, token, entry_id):
        if token not in self.postings:
            self.postings[token] = []
        self.postings[token].append(entry_id)
