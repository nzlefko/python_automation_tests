from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Launch browser
driver = webdriver.Chrome()
driver.get("https://automationexercise.com")

# Maximize window
driver.maximize_window()

# Click on the 'Products' page
driver.find_element(By.PARTIAL_LINK_TEXT, "Products").click()
time.sleep(2)

# Search for a product
search_box = driver.find_element(By.ID, "search_product")
search_box.send_keys("Tshirt")
search_box.send_keys(Keys.RETURN)
time.sleep(2)

# Locate the 'Searched Products' section
searched_products_section = driver.find_element(By.CLASS_NAME, "features_items")

# Within this section, find all product elements
product_elements = searched_products_section.find_elements(By.CLASS_NAME, "product-image-wrapper")

visible_products = [p for p in product_elements if p.is_displayed()]

# Output the count of products found
print(f"Number of products found: {len(visible_products)}")

# Close the browser
driver.quit()
