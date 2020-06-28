__all__ = ["client"]

import pytest
from flask.testing import FlaskClient

from main.app import app


@pytest.fixture
def client() -> FlaskClient:
    app_context = app.app_context()
    app_context.push()
    client = app.test_client()
    yield client
    app_context.pop()
