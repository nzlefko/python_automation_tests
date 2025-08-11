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

def test_post_to_search_product_without_search_product_negative():
    endpoint = f"{BASE_URL}/searchProduct"
    # data = {
    #     "search_product": "",
    # }

    response = requests.post(endpoint)
    assert response.status_code == 400
    assert response.text == "Bad request, search_product parameter is missing in POST request."