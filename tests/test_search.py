from config import SEARCH_TERM
from helpers.navigation import navigate_to_products_page
from helpers.navigation import navigate_to_contact_page
from helpers.product_helpers import search_for_product, get_visible_search_results

def test_search_product(driver):
    navigate_to_products_page(driver)
    search_for_product(driver, SEARCH_TERM)
    results = get_visible_search_results(driver)
    assert len(results) > 0, f"No results found for: {SEARCH_TERM}"

    driver.quit()