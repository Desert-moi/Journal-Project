from db.repository import *
import mysql.connector


class MysqlRepository(Repository):

    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'AZpassword',
            'host': 'localhost',  # db  OR to run LOCALLY, this should be localhost
            'port': '32006',  # 3306 OR to run LOCALLY, this should be 32001
            'database': 'journal_entries'
        }

        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()
        
    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def mapper(self, entry: dict) -> JournalEntry:
        return JournalEntry(
            jid=entry['jid'],
            person_id=entry['person_id'],
            text=entry['text'],
            date_written=entry['date_written'],
            author=entry['author'],
            text_keyword=entry['text_keyword'],
            location=entry['location']
        )

    def load_journals(self) -> list[JournalEntry]:
        sql = 'SELECT * FROM journal'
        self.cursor.execute(sql)
        entries = self.cursor.fetchall()
        return [self.mapper(entry) for entry in entries]
