from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.CalculatorPage import CalculatorPage
import allure


@allure.id("SKYPRO-1")
@allure.story("")
@allure.epic("онлайн-калькулятор https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
@allure.title("Тестирование калькулятора")
@allure.severity("blocker")
def test_calculator():
    """
    Тест на проверку вычисления калькулятора, результат должен ==15
    """
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    with allure.step("Открытие страницы калькулятора"):
        calc_page = CalculatorPage(browser)

    with allure.step("Внесение значения 45 в поле задержки (локатор #delay)"):
        calc_page.test_delay()

    with allure.step("Нажать кнопки: 7, +, 8, = "):
        calc_page.test_calc()

    with allure.step("Проверить (assert), что в окне отобразится результат 15 через 45 секунд"):
        to_be = calc_page.test_result()
        as_is = 15
        assert as_is == to_be

    browser.quit()
