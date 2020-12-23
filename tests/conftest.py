import pytest
from app import app as app_


@pytest.fixture
def client():
    return app_.test_client()
