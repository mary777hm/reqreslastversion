import pytest
import requests

@pytest.fixture
def api_client():
    session = requests.Session()
    yield session
    session.close()

@pytest.fixture
def base_url():
    return "https://reqres.in/api"