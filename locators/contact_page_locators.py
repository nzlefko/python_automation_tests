from selenium.webdriver.common.by import By

class ContactPageLocators:
    INPUT_NAME = (By.NAME, "name")
    INPUT_EMAIL = (By.NAME, "email")
    INPUT_SUBJECT = (By.NAME, "subject")
    INPUT_MESSAGE = (By.NAME, "message")
    UPLOAD_BUTTON = (By.NAME, "upload_file")
    SUBMIT_BUTTON = (By.NAME, "submit")
