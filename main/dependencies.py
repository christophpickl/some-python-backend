from dependency_injector import providers, containers

from .logic import InMemoryBookRepository, BookService


class Dependencies(containers.DeclarativeContainer):
    bookRepository = providers.Singleton(InMemoryBookRepository)
    bookService = providers.Singleton(BookService, repo = bookRepository)

