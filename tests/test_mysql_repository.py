from db.mysql_repository import *

repo = MysqlRepository()

journal_entry = {'jid': 4,
                 'text': 'Spent the day hiking in the mountains. The scenery was breathtaking, and the fresh air was invigorating. It was a great way to disconnect from work and enjoy nature. I took plenty of photos to remember the experience. Returned home in the evening, feeling refreshed and relaxed.',
                'date_written': '2024-07-20 17:00:00',
                'author': 'Gabriel Doesgood',
                'text_keyword': 'hiking, nature, photography, relaxation',
                'location': 'Denver, USA'
                 }


def test_jid():
    jid = repo.mapper(journal_entry)
    assert jid == '4'
