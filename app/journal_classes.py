from dataclasses import dataclass


@dataclass
class JournalEntry:
    def __init__(self, text, date_written, author, text_keyword, location):
        self.text = text
        self.date_written = date_written
        self.author = author
        self.text_keyword = text_keyword
        self.location = location

    def get_author(self):
        return self.author

    def get_date_written(self):
        return self.date_written

    def get_location(self):
        return self.location

    def get_text(self):
        return self.text

    def get_text_keyword(self):
        return self.text_keyword

    def __repr__(self):
        return (f"JournalEntry(text='{self.text}', date_written={self.date_written}, "
                f"author='{self.author}', text_keyword='{self.text_keyword}', "
                f"location='{self.location}')")
