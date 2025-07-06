from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL
from locators.navigation_locators import NavigationLocators
from locators.product_locators import ProductLocators

def navigate_to_products_page(driver):
    driver.get(BASE_URL)
    NavigationLocators.PRODUCT_LINK.click()

def navigate_to_contact_page(driver):
    driver.get(BASE_URL)

    contact_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(NavigationLocators.CONTACT_US_LINK)
        )
    contact_link.click()

#def fill_contact_us_form(driver):

