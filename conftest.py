import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture
def driver():
    # Dynamically build the path to chromedriver inside the project
    driver_path = os.path.join(os.getcwd(), "drivers", "chromedriver","chromedriver-mac-x64", "chromedriver")
    service = ChromeService(executable_path=driver_path)

    # Initialize WebDriver with custom service
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)

    yield driver
    driver.quit()