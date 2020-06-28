from abc import ABC, abstractmethod


class BookRepository(ABC):
    @abstractmethod
    def all(self):
        pass


books = [
    {
        'id': 1,
        'title': 'Clean Code'
    },
    {
        'id': 2,
        'title': 'Pragmatic Programmer'
    }
]


class InMemoryBookRepository(BookRepository):
    def all(self):
        return books


class BookService:
    def __init__(self, repo: BookRepository):
        self.repo = repo

    def all(self):
        return self.repo.all()

