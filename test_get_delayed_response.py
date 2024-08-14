import requests
import allure
import pytest


@allure.feature("User Management")
@allure.story("Delayed Response")
@allure.title("Delayed Response for List Users")
def test_delayed_response(api_client, base_url):
    url = f"{base_url}/users?delay=3"

    response = api_client.get(url)

    assert response.status_code == 200
    response_json = response.json()

    assert response_json['page'] == 1
    assert response_json['per_page'] == 6
    assert response_json['total'] == 12
    assert response_json['total_pages'] == 2

    expected_data = [
        {
            "id": 1,
            "email": "george.bluth@reqres.in",
            "first_name": "George",
            "last_name": "Bluth",
            "avatar": "https://reqres.in/img/faces/1-image.jpg"
        },
        {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        },
        {
            "id": 3,
            "email": "emma.wong@reqres.in",
            "first_name": "Emma",
            "last_name": "Wong",
            "avatar": "https://reqres.in/img/faces/3-image.jpg"
        },
        {
            "id": 4,
            "email": "eve.holt@reqres.in",
            "first_name": "Eve",
            "last_name": "Holt",
            "avatar": "https://reqres.in/img/faces/4-image.jpg"
        },
        {
            "id": 5,
            "email": "charles.morris@reqres.in",
            "first_name": "Charles",
            "last_name": "Morris",
            "avatar": "https://reqres.in/img/faces/5-image.jpg"
        },
        {
            "id": 6,
            "email": "tracey.ramos@reqres.in",
            "first_name": "Tracey",
            "last_name": "Ramos",
            "avatar": "https://reqres.in/img/faces/6-image.jpg"
        }
    ]

    assert response_json['data'] == expected_data
    assert response_json['support']['url'] == "https://reqres.in/#support-heading"
    assert response_json['support'][
               'text'] == "To keep ReqRes free, contributions towards server costs are appreciated!"