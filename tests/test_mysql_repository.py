from db.mysql_repository import *


def test_database():
    repo = MysqlRepository()

    # Check that is a repository
    assert isinstance(repo, Repository)

    # Loads repository
    entries = repo.load_journals()

    # Check that entries is a list
    assert isinstance(entries, list)

    # Checks that we have some entries
    assert len(entries) > 0

    # Example checks to verify specific information
    assert any(entry.get_author() == 'Janey Jackay' for entry in entries)
    assert any(entry.get_location() == 'Chicago, USA' for entry in entries)
    assert any('yoga' in entry.get_text() for entry in entries)
    assert any('project proposal' in entry.get_text_keyword() for entry in entries)
