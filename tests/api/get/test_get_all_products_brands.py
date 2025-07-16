import requests
from tests.api.config.api_constants import BASE_URL

def test_get_all_products():
    response = requests.get(f"{BASE_URL}/productsList")

    assert response.status_code == 200
    assert "products" in response.json()

def test_get_all_brands():
    response = requests.get(f"{BASE_URL}/brandsList")

    assert response.status_code == 200
    assert "brands" in response.json()
