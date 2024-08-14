import requests
import pytest
import allure


@allure.feature("Get List Users")
@allure.story("Retrieve a list of users from the second page")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_get_list_users():
    url = "https://reqres.in/api/users?page=2"

    with allure.step("Sending GET request to retrieve list of users"):
        response = requests.get(url)

    with allure.step("Validating the response status code"):
        assert response.status_code == 200, "Expected status code 200"

    with allure.step("Validating the response body"):
        expected_response = {
            "page": 2,
            "per_page": 6,
            "total": 12,
            "total_pages": 2,
            "data": [
                {"id": 7, "email": "michael.lawson@reqres.in", "first_name": "Michael", "last_name": "Lawson",
                 "avatar": "https://reqres.in/img/faces/7-image.jpg"},
                {"id": 8, "email": "lindsay.ferguson@reqres.in", "first_name": "Lindsay", "last_name": "Ferguson",
                 "avatar": "https://reqres.in/img/faces/8-image.jpg"},
                {"id": 9, "email": "tobias.funke@reqres.in", "first_name": "Tobias", "last_name": "Funke",
                 "avatar": "https://reqres.in/img/faces/9-image.jpg"},
                {"id": 10, "email": "byron.fields@reqres.in", "first_name": "Byron", "last_name": "Fields",
                 "avatar": "https://reqres.in/img/faces/10-image.jpg"},
                {"id": 11, "email": "george.edwards@reqres.in", "first_name": "George", "last_name": "Edwards",
                 "avatar": "https://reqres.in/img/faces/11-image.jpg"},
                {"id": 12, "email": "rachel.howell@reqres.in", "first_name": "Rachel", "last_name": "Howell",
                 "avatar": "https://reqres.in/img/faces/12-image.jpg"}
            ],
            "support": {
                "url": "https://reqres.in/#support-heading",
                "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
            }
        }

        assert response.json() == expected_response, "Response body does not match expected response"

    with allure.step("Logging the response"):
        allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.JSON)