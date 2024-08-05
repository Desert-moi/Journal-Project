from _datetime import datetime
from app.journal_classes import *


# Test JournalEntry class
def test_journal_entry():
    test_entry = JournalEntry("Sample text", datetime(2023, 7, 21), "Author", "keyword1, keyword2", "Location")
    assert test_entry.text == "Sample text"
    assert test_entry.date_written == datetime(2023, 7, 21)
    assert test_entry.author == "Author"
    assert test_entry.text_keyword == "keyword1, keyword2"
    assert test_entry.location == "Location"


