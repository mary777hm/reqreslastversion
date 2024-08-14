import requests
import allure
import pytest


@allure.feature("User Management")
@allure.story("User Registration")
@allure.title("Register User Unsuccessfully - Missing Password")
def test_register_user_failure(base_url):
    url = f"{base_url}/register"
    payload = {
        "email": "sydney@fife"
    }
    response = requests.post(url, json=payload)

    assert response.status_code == 400
    assert response.json() == {"error": "Missing password"}