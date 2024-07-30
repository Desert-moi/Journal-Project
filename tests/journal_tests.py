from _datetime import datetime
from app.journal_classes import *


# Test JournalEntry class
def test_journal_entry():
    test_entry = JournalEntry(1, "Sample text", datetime(2023, 7, 21), "Author", "keyword1, keyword2", "Location")
    assert test_entry.id == 1
    assert test_entry.text == "Sample text"
    assert test_entry.date_written == datetime(2023, 7, 21)
    assert test_entry.author == "Author"
    assert test_entry.text_keyword == "keyword1, keyword2"
    assert test_entry.location == "Location"


# Test Journal class
journal = Journal()
entry = JournalEntry(2, "Another text", datetime(2023, 7, 22), "Author2", "keyword3, keyword4", "Location2")
journal.add_entry(entry)
assert entry in journal.journal_entries

# Test Token class
token = Token("sample")
assert token.term == "sample"

# Test TermDocumentIndex class
tdi = TermDocumentIndex()
token = Token("sample")
tdi.add_to_vocabulary(token)
assert token in tdi.vocabulary

tdi.add_posting(token, 1)
assert 1 in tdi.postings[token]
