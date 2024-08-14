import requests
import pytest
import allure

BASE_URL = "https://reqres.in/api"


@pytest.mark.register
@allure.feature("User Management")
@allure.story("User Registration")
@allure.title("Register User Successfully")
def test_register_user():
    endpoint = "/register"
    url = f"{BASE_URL}{endpoint}"
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 200
    response_json = response.json()
    assert "id" in response_json
    assert "token" in response_json