import requests
import allure
import pytest


@allure.feature("User Management")
@allure.story("User Login")
@allure.title("Login User Successfully")
def test_login_successful(api_client, base_url):
    url = f"{base_url}/login"
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }


    response = api_client.post(url, json=payload)


    assert response.status_code == 200
    response_data = response.json()
    assert "token" in response_data
    assert response_data["token"] == "QpwL5tke4Pnpja7X4"