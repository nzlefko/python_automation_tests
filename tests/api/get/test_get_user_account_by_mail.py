import requests
from tests.api.config.api_constants import BASE_URL
from test_data import *

def test_get_account_detail_by_mail():
    endpoint = f"{BASE_URL}/getUserDetailByEmail"
    params = {
        "email": CONTACT_EMAIL,
        "password": VALID_PASSWORD
    }

    response = requests.get(endpoint, params=params)

    assert response.status_code == 200
    assert "email" in response.text

def test_get_account_detail_by_mail_negative():
    endpoint = f"{BASE_URL}/getUserDetailByEmail"
    params = {
        "email": INVALID_EMAIL,
        "password": INVALID_PASSWORD
    }

    response = requests.get(endpoint, params=params)

    assert response.status_code == 404
    assert "email" in response.text