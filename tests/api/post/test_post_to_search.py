import requests
from tests.api.config.api_constants import BASE_URL
from test_data import *

def test_post_to_search_product():
    endpoint = f"{BASE_URL}/searchProduct"
    data = {
        "search_product": "jeans",
    }

    response = requests.post(endpoint, data=data)
    assert response.status_code == 200
    assert "products" in response.json()
    assert len(response.json()["products"]) == 3