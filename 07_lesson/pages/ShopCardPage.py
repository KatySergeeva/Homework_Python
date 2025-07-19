from selenium.webdriver.common.by import By


class ShopCardPage:

    def __init__(self, browser):
        self._driver = browser

    def checkout(self):
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self._driver.find_element(By.ID, "checkout").click()
