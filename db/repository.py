import abc
from app.journal_classes import *


class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_journals(self) -> list[JournalEntry]:
        raise NotImplementedError
