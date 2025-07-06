from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL, IMPLICIT_WAIT
from locators.product_locators import ProductLocators


def start_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(IMPLICIT_WAIT)
    driver.maximize_window()
    return driver

def search_for_product(driver, query):
    driver.get(BASE_URL)

    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(ProductLocators.SEARCH_INPUT)
    )
    search_box.send_keys(query)

    search_button = driver.find_element(*ProductLocators.SEARCH_BUTTON)
    search_button.click()

def get_visible_search_results(driver):
    return driver.find_elements(ProductLocators.PRODUCT_RESULT)