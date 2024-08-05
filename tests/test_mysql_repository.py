from db.mysql_repository import *


def test_database():
    repo = MysqlRepository()
    assert isinstance(repo, Repository)

    entry = {
        'jid': 1,
        'person_id': 42,
        'text': 'Sample journal text',
        'date_written': '2024-08-01',
        'author': 'Arthur Naim',
        'text_keyword': 'Sample',
        'location': 'Nowhere, AZ'
    }
    journal_entry = repo.mapper(entry)

    assert journal_entry.jid == 1
    assert journal_entry.person_id == 42
    assert journal_entry.text == 'Sample journal text'
    assert journal_entry.date_written == '2024-08-01'
    assert journal_entry.author == 'Arthur Naim'
    assert journal_entry.text_keyword == 'Sample'
    assert journal_entry.location == 'Nowhere, AZ'