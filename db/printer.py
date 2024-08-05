from db.mysql_repository import *


def print_db():
    repo = MysqlRepository()
    entries = repo.load_journals()
    for entry in entries:
        print(entry)
        print(type(entry))


print_db()
