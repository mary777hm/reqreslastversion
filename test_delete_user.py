import requests
import allure
import pytest

@allure.feature("User Management")
@allure.story("User Deletion")
@allure.title("Delete User")
def test_delete_user(api_client, base_url):
    user_id = 2
    url = f"{base_url}/users/{user_id}"


    get_response = api_client.get(url)
    assert get_response.status_code == 200
    user_data = get_response.json()
    assert user_data['data']['id'] == user_id
    assert user_data['data']['email'] == "janet.weaver@reqres.in"
    assert user_data['data']['first_name'] == "Janet"
    assert user_data['data']['last_name'] == "Weaver"
    assert user_data['data']['avatar'] == "https://reqres.in/img/faces/2-image.jpg"


    delete_response = api_client.delete(url)


    assert delete_response.status_code == 204
    assert delete_response.text == ''