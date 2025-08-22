from selenium.webdriver.common.by import By


class ShopCardPage:
    """
    Класс для работы с корзиной
    """

    def __init__(self, browser):
        self._driver = browser

    def checkout(self):
        """
        Скроллим страницу вниз и нажимаем "checkout" для перехода в раздел внесения данных о покупателе
        """
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self._driver.find_element(By.ID, "checkout").click()
