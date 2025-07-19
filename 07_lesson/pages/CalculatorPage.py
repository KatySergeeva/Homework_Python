from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(30)

    def test_delay(self):
        self._driver.get(" https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        delay = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        delay.clear()
        delay.send_keys(45)

    def test_calc(self):
        seven = self._driver.find_element(By.XPATH, "//span[text()='7']")
        seven.click()

        plus = self._driver.find_element(By.XPATH, "//span[text()= '+']")
        plus.click()

        eight = self._driver.find_element(By.XPATH, "//span[text()='8']")
        eight.click()

        equals = self._driver.find_element(By.XPATH, "//span[text()= '=']")
        equals.click()

    def test_result(self):
        waiter = WebDriverWait(self._driver, 50, 0.1)
        waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
        result = self._driver.find_element(By.CSS_SELECTOR, ".screen").text
        return int(result)
