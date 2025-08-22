from selenium.webdriver.common.by import By


class ShopOrderPage:
    """
    Класс по работе со страницей внесения информации о покупателе"""

    def __init__(self, browser):
        self._driver = browser

    def data_registration(self):
        """Внести данные (first-name, last-name, postal-code )"""
        self._driver.find_element(By.ID, "first-name").send_keys("Екатерина")
        self._driver.find_element(By.ID, "last-name").send_keys("Сергеева")
        self._driver.find_element(By.ID, "postal-code").send_keys("443543")

        """Нажать continue"""
        self._driver.find_element(By.ID, "continue").click()

    def total_sum(self):
        """Получить значение Total со страницы """
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        total = self._driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
        clean_total = total.replace('Total: $', '').strip()
        return clean_total
