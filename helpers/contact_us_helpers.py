from locators.contact_page_locators import ContactPageLocators
from test_data import *
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def fill_contact_us_form(driver):
 driver.find_element(*ContactPageLocators.INPUT_NAME).send_keys(CONTACT_NAME)
 driver.find_element(*ContactPageLocators.INPUT_EMAIL).send_keys(CONTACT_EMAIL)
 driver.find_element(*ContactPageLocators.INPUT_SUBJECT).send_keys(CONTACT_SUBJECT)
 driver.find_element(*ContactPageLocators.INPUT_MESSAGE).send_keys(CONTACT_MESSAGE)
 driver.find_element(*ContactPageLocators.SUBMIT_BUTTON).click()
 try:
     alert = driver.switch_to.alert
     alert.accept()
 except NoAlertPresentException:
     print("No alert appeared")
     #
     # success_message = WebDriverWait(driver, 10).until(
     #   EC.visibility_of_element_located((By.CLASS_NAME, "status alert alert-success"))
     # )
     # return success_message

def fill_contact_us_form_and_upload_file(driver):
  driver.find_element(*ContactPageLocators.INPUT_NAME).send_keys(CONTACT_NAME)
  driver.find_element(*ContactPageLocators.INPUT_EMAIL).send_keys(CONTACT_EMAIL)
  driver.find_element(*ContactPageLocators.INPUT_SUBJECT).send_keys(CONTACT_SUBJECT)
  driver.find_element(*ContactPageLocators.INPUT_MESSAGE).send_keys(CONTACT_MESSAGE)
  driver.find_element(*ContactPageLocators.UPLOAD_BUTTON).send_keys(UPLOAD_FILE_PATH)
  driver.find_element(*ContactPageLocators.SUBMIT_BUTTON).click()
  try:
      alert = driver.switch_to.alert
      alert.accept()
  except NoAlertPresentException:
    print("No alert appeared")
    #
    # success_message = WebDriverWait(driver, 10).until(
    #          EC.visibility_of_element_located((By.CSS_SELECTOR, ".status.alert.alert-success"))
    #      )
    # return success_message