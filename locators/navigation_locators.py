from selenium.webdriver.common.by import By

class NavigationLocators:
    CONTACT_US_LINK = (By.LINK_TEXT, "Contact us")
    GET_IN_TOUCH_HEADER = (By.XPATH, "//h2[text()='Get In Touch']")
    PRODUCT_LINK = (By.LINK_TEXT, "Product")
    CART_LINK = (By.PARTIAL_LINK_TEXT, "Cart")

