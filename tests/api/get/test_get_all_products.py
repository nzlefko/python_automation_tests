import requests
from tests.api.config.api_constants import BASE_URL


def test_get_all_products():
    response = requests.get(f"{BASE_URL}/productsList")

    assert response.status_code == 200
    assert "products" in response.json()
