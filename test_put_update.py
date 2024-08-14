import requests
import pytest
import allure

BASE_URL = "https://reqres.in/api"

@pytest.mark.update
@allure.feature("User Management")
@allure.story("Update User")
@allure.title("Update User with valid data")
def test_put_update_user():
    endpoint = "/users/2"
    url = f"{BASE_URL}{endpoint}"

    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }

    response = requests.put(url, json=payload)
    assert response.status_code == 200

    json_response = response.json()
    assert json_response["name"] == "morpheus"
    assert json_response["job"] == "zion resident"
    assert "updatedAt" in json_response