import requests
from tests.api.config.api_constants import BASE_URL
from test_data import *

def test_invalid_login_credentials():
    endpoint = f"{BASE_URL}/verifyLogin"

    payload = {
        "email": INVALID_EMAIL,
        "password": INVALID_PASSWORD,
    }

    response = requests.post(endpoint, data=payload)
    assert "User not found!" in response.json().get("message")