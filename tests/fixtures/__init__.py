__all__ = ["client"]

import pytest

from main.app import app


@pytest.fixture
def client():
    app_context = app.app_context()
    app_context.push()
    client = app.test_client()
    yield client
    app_context.pop()

