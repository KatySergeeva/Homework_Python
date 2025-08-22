from selenium.webdriver.common.by import By


class ShopMainPage:

    """
    Класс по работе с главной страницей
    """

    def __init__(self, driver):
        self._driver = driver

    def add_card(self):
        """
        Добавление товаров в корзину
        """
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        
    def go_to_card(self):
        """
        Переход на страницу корзины
        """
        self._driver.get("https://www.saucedemo.com/cart.html")
