from selenium.webdriver.common.by import By

class ProductLocators:
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='button']")
    PRODUCT_RESULT = (By.CSS_SELECTOR, ".features_items .product-image-wrapper")
    SEARCH_HEADER = (By.XPATH, "//h2[text()='Searched Products']")
