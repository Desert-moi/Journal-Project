from app.services import *
from db.mysql_repository import *


def test_services():
    s = Services()
    # Checks if repo is an instance of MysqlRepository
    assert isinstance(s.repo, MysqlRepository)

    # sets a target author on the services instance s
    target_author = "Janey Jackay"
    recall = s.recall_author(target_author)

    # this should return as a list of items and there should be only two entries.
    assert isinstance(recall, list)
    assert len(recall) == 2

    # Checks if 'Janey Jackay' is found in the returned statements
    assert any(entry.get_author() == 'Janey Jackay' for entry in recall)

    # Checks if 'Chicago, USA' is in the journal entries as this is the location of Janey
    assert any(entry.get_location() == 'Chicago, USA' for entry in recall)

    # Checks if another author was called

    assert any(entry.get_author() != 'Bob Bert' or 'Liam Strongman' or 'Gabriel Doesgood' or 'Francisco Holdon' for entry in recall)


