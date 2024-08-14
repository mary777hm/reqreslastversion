import requests
import pytest
import allure

BASE_URL = "https://reqres.in/api"

@pytest.mark.create
@allure.feature("User Management")
@allure.story("Create User")
@allure.title("Create User with valid data")
def test_post_create_user():
    endpoint = "/users"
    url = f"{BASE_URL}{endpoint}"

    payload = {
        "name": "morpheus",
        "job": "leader"
    }

    response = requests.post(url, json=payload)
    assert response.status_code == 201

    json_response = response.json()
    assert json_response["name"] == "morpheus"
    assert json_response["job"] == "leader"
    assert "id" in json_response
    assert "createdAt" in json_response