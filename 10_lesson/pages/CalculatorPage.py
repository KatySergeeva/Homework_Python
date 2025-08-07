from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    """
    Это класс по работе с калькулятором
    """

    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(30)

    def test_delay(self):
        """
        Увеличиваем время ожидания результата решения до 45 секунд в поле задержки
        """
        self._driver.get(" https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        delay = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        delay.clear()
        delay.send_keys(45)

    def test_calc(self):
        """
        Нажимаем поочередно элементы для вычисления решения(значения элементов: 7, +, 8, =)
        """
        seven = self._driver.find_element(By.XPATH, "//span[text()='7']")
        seven.click()

        plus = self._driver.find_element(By.XPATH, "//span[text()= '+']")
        plus.click()

        eight = self._driver.find_element(By.XPATH, "//span[text()='8']")
        eight.click()

        equals = self._driver.find_element(By.XPATH, "//span[text()= '=']")
        equals.click()

    def test_result(self):
        """
        Возвращаем результат вычисления калькулятора
        """
        waiter = WebDriverWait(self._driver, 50, 0.1)
        waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
        result = self._driver.find_element(By.CSS_SELECTOR, ".screen").text
        return int(result)
