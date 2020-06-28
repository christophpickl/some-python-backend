from main.logic import BookService, InMemoryBookRepository


class TestBookService:
    def test_all_returns_something(self):
        service = BookService(InMemoryBookRepository())
        assert len(service.all()) > 0

