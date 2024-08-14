import requests
import pytest
import allure

BASE_URL = "https://reqres.in/api"

@allure.feature("Get Single User")
@allure.story("User Not Found")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_get_single_user_not_found():
    response = requests.get(f"{BASE_URL}/users/23")
    assert response.status_code == 404
    assert response.json() == {}