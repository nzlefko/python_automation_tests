import time
from helpers.contact_us_helpers import *
from helpers.navigation import navigate_to_contact_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.contact_page_locators import ContactPageLocators
from test_data import *
from selenium.common.exceptions import NoAlertPresentException

def test_contact_us_page(driver):
    navigate_to_contact_page(driver)

    heading = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[text()='Get In Touch']"))
    )

    assert heading is not None

def test_contact_us_submit(driver):
    navigate_to_contact_page(driver)
    fill_contact_us_form(driver)
    time.sleep(2)
    SuccessBtn = driver.find_element(By.XPATH, "//*[@id='form-section']/a")
    assert SuccessBtn is not None

def test_contact_us_file_upload(driver):
    navigate_to_contact_page(driver)
    fill_contact_us_form_and_upload_file(driver)
    time.sleep(2)
    SuccessBtn = driver.find_element(By.XPATH, "//*[@id='form-section']/a")
    assert SuccessBtn is not None