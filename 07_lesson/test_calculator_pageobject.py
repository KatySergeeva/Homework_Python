from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.CalculatorPage import CalculatorPage


def test_calculator():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    calc_page = CalculatorPage(browser)
    calc_page.test_delay()
    calc_page.test_calc()
    to_be = calc_page.test_result()
    as_is = 15
    assert as_is == to_be

    browser.quit()
