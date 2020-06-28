from main.logic import BookRepository


class BookRepositoryStub(BookRepository):
    def __init__(self, data):
        self.data = data

    def all(self):
        return self.data
