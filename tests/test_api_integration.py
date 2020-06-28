from dependency_injector import providers
from flask import json

from main.dependencies import Dependencies
from tests.stubs import BookRepositoryStub


class TestEndpoints:

    def test_root(self, client):
        response = client.get("/")

        assert b'hello flask' in response.data
        assert response.status_code == 200

    def test_books(self, client):
        test_book = {'id': 42, 'title': 'test_title'}
        Dependencies.bookRepository.override(providers.Factory(BookRepositoryStub, data=[test_book]))

        response = client.get("/api/v1/books")

        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) == 1
        assert data[0]["id"] == test_book["id"]
        assert data[0]["title"] == test_book["title"]

    def test_debug_option(self, client):
        response = client.get("/", query_string={"debug": "1"})

        assert response.status_code == 200
        assert response.headers.getlist('magic-flask') == ['foobar']
