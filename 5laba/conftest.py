import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture
def session():
    with requests.Session() as s:
        yield s
