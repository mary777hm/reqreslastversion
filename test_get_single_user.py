import requests
import pytest
import allure

BASE_URL = "https://reqres.in/api"


@allure.feature("Get Single User")
@allure.story("Retrieve a single user by ID")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
def test_get_single_user():
    user_id = 2
    endpoint = f"/users/{user_id}"
    url = f"{BASE_URL}{endpoint}"

    with allure.step(f"Sending GET request to retrieve user with ID {user_id}"):
        response = requests.get(url)

    with allure.step("Validating the response status code"):
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    with allure.step("Validating the response body"):
        expected_response = {
            "data": {
                "id": 2,
                "email": "janet.weaver@reqres.in",
                "first_name": "Janet",
                "last_name": "Weaver",
                "avatar": "https://reqres.in/img/faces/2-image.jpg"
            },
            "support": {
                "url": "https://reqres.in/#support-heading",
                "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
            }
        }

        assert response.json() == expected_response, "Response body does not match expected response"

    with allure.step("Logging the response"):
        allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.JSON)