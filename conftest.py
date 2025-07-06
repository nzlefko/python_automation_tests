# conftest.py
import pytest
from selenium import webdriver
from config import IMPLICIT_WAIT

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(IMPLICIT_WAIT)
    driver.maximize_window()
    yield driver
    driver.quit()
