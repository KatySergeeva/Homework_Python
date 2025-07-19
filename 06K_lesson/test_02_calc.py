from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(30)
    yield driver


@pytest.mark.usefixtures("driver")
def test_calc(driver):
    driver.get(" https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    delay = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay.clear()
    delay.send_keys(45)

    seven = driver.find_element(By.XPATH, "//span[text()='7']")
    seven.click()

    plus = driver.find_element(By.XPATH, "//span[text()= '+']")
    plus.click()

    eight = driver.find_element(By.XPATH, "//span[text()='8']")
    eight.click()

    equals = driver.find_element(By.XPATH, "//span[text()= '=']")
    equals.click()

    waiter = WebDriverWait(driver, 50, 0.1)
    waiter.until(
        EC.text_to_be_present_in_element( (By.CSS_SELECTOR, ".screen"), "15")
    )
    result = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert int(result) == 15
    driver.quit()
