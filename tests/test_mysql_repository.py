from db.mysql_repository import *


def test_database():
    repo = MysqlRepository()
    assert isinstance(repo, Repository)