import requests
import allure
import pytest


@allure.feature("User Management")
@allure.story("User Login")
@allure.title("Login User Unsuccessfully - Missing Password")
def test_login_unsuccessful(api_client, base_url):
    url = f"{base_url}/login"
    payload = {
        "email": "peter@klaven"
    }


    response = api_client.post(url, json=payload)


    assert response.status_code == 400
    response_data = response.json()
    assert "error" in response_data
    assert response_data["error"] == "Missing password"