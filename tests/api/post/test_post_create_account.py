import requests
from tests.api.config.api_constants import BASE_URL
from test_data import *

def test_create_account():
    endpoint = f"{BASE_URL}/createAccount"

    payload = {
        "name": "Naftaly Tester",
        "email": "some_new_email@example.com",
        "password": VALID_PASSWORD,
        "title": "Mr",
        "birth_date": "10",
        "birth_month": "January",
        "birth_year": "1990",
        "firstname": "Naftaly",
        "lastname": "Tester",
        "company": "Test Company",
        "address1": "123 Test Street",
        "address2": "Apt 4B",
        "country": "United States",
        "zipcode": "10001",
        "state": "NY",
        "city": "New York",
        "mobile_number": "123-456-7890"
    }

    response = requests.post(endpoint, data=payload)
    assert response.json().get("responseCode") == 201
    assert "User created!" in response.json().get("message")

def test_delete_account():
    endpoint = f"{BASE_URL}/deleteAccount"

    payload = {
        "email": "some_new_email@example.com",
        "password": VALID_PASSWORD
    }

    response = requests.delete(endpoint, data=payload)
    assert response.json().get("responseCode") == 200
    assert "Account deleted!" in response.json().get("message")
