import keyword
from datetime import date

from db.repository import *
import mysql.connector


class MysqlRepository(Repository):

    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',  # db  OR to run LOCALLY, this should be localhost
            'port': '32001',  # 3306 OR to run LOCALLY, this should be 32001
            'database': 'journal_entries'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def mapper(self, entry: dict) -> JournalEntry:
        journal_entry = JournalEntry(jid=entry.get('jid'),
                                     text=entry.get('text'),
                                     date_written=entry.get('date_written'),
                                     author=entry.get('author'),
                                     text_keyword=entry.get('text_keyword'),
                                     location=entry.get('location'))
        return journal_entry

    def load_journals(self) -> list[JournalEntry]:
        sql = 'SELECT * FROM journal'
        self.cursor.execute(sql)
        entries = [{'jid': jid,
                    'person_id': person_id,
                    'text': text,
                    'date_written': date_written,
                    'author': author,
                    'text_keyword': text_keyword,
                    'location': location
                    } for (jid, person_id, text, date_written, author, text_keyword, location) in self.cursor]
        journal = [self.mapper(entry) for entry in entries]
        return journal
