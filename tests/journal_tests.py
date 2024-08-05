from _datetime import datetime
from app.journal_classes import *


# Test JournalEntry class
def test_journal_entry():
    test_entry = JournalEntry(1, 101, "Sample text", datetime(2023, 7, 21), "Author", "keyword1, keyword2", "Location")
    assert test_entry.jid == 1
    assert test_entry.person_id == 101
    assert test_entry.text == "Sample text"
    assert test_entry.date_written == datetime(2023, 7, 21)
    assert test_entry.author == "Author"
    assert test_entry.text_keyword == "keyword1, keyword2"
    assert test_entry.location == "Location"


