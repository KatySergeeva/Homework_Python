from selenium.webdriver.common.by import By


class ShopMainPage:

    def __init__(self, driver):
        self._driver = driver

    def add_card(self):
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        

    def go_to_card(self):
        self._driver.get("https://www.saucedemo.com/cart.html")
