from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


@dataclass
class Book:
    id: int
    title: str


class BookRepository(ABC):
    @abstractmethod
    def all(self) -> List[Book]:
        pass


class InMemoryBookRepository(BookRepository):
    books: List[Book] = [
        Book(id=1, title="Clean Code"),
        Book(id=2, title="Pragmatic Programmer")
    ]

    def all(self) -> List[Book]:
        return self.books


class BookService:
    def __init__(self, repo: BookRepository):
        self.repo = repo

    def all(self) -> List[Book]:
        return self.repo.all()
