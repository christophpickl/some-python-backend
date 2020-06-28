# noinspection PyUnresolvedReferences
from flask import json

# noinspection PyUnresolvedReferences
from tests.fixtures import client


class TestEndpoints:
    def test_root(self, client):
        response = client.get("/")
        assert b'hello flask' in response.data
        assert response.status_code == 200

    def test_books(self, client):
        response = client.get("/api/v1/books")
        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) == 2
        assert data[0]["id"] == 1
        assert data[0]["title"] == "Clean Code"

    def test_debug_option(self, client):
        response = client.get("/", query_string={"debug": "1"})
        assert response.status_code == 200
        assert response.headers.getlist('magic-flask') == ['foobar']

