from db.repository import *
import pymysql


class MysqlRepository(Repository):
    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'AZpassword',
            'host': 'localhost',
            'port': 3306,
            'database': 'Journals'
        }

        self.connection = pymysql.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    @staticmethod
    def mapper(entry):
        return JournalEntry(
            text=entry[0],
            date_written=entry[1],
            author=entry[2],
            text_keyword=entry[3],
            location=entry[4],
        )

    def load_journals(self) -> list[JournalEntry]:
        sql = 'SELECT * FROM Journal_Entries'
        self.cursor.execute(sql)
        entries = self.cursor.fetchall()
        return [self.mapper(entry) for entry in entries]
