import requests
import pytest
import allure

BASE_URL = "https://reqres.in/api"

@pytest.mark.update
@allure.feature("User Management")
@allure.story("Patch User")
@allure.title("Patch User with valid data")
def test_patch_update_user():
    endpoint = "/users/2"
    url = f"{BASE_URL}{endpoint}"

    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }

    response = requests.patch(url, json=payload)
    assert response.status_code == 200

    json_response = response.json()
    assert json_response["name"] == "morpheus"
    assert json_response["job"] == "zion resident"
    assert "updatedAt" in json_response