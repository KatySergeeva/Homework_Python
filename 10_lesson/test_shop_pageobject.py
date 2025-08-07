from selenium import webdriver
import pytest
from pages.ShopAuthorizationPage import ShopAuthorizationPage
from pages.ShopMainPage import ShopMainPage
from pages.ShopCardPage import ShopCardPage
from pages.ShopOrderPage import ShopOrderPage
import allure


@allure.id("SKYPRO-2")
@allure.story("")
@allure.epic("интеренет-магазин http://www.saucedemo.com")
@allure.title("Тестирование интернет-магазина")
@allure.severity("blocker")
def test_shop():
    """
    Тест работы интернет-магазина
    """
    browser = webdriver.Firefox()

    with allure.step("Авторизация"):
        authorization_page = ShopAuthorizationPage(browser)
        authorization_page.authorization()

    with allure.step("Добавление товаров в корзину"):
        main_page = ShopMainPage(browser)
        main_page.add_card()
        main_page.go_to_card()

    with allure.step("Переход в корзину и после переход к оформлению"):
        card_page = ShopCardPage(browser)
        card_page.checkout()

    with allure.step("Внесение данных покупателя для оформления заказа"):
        order_page = ShopOrderPage(browser)
        order_page.data_registration()

    with allure.step("Получение данных о сумме Total и проверка со значением 58.29"):
        total = order_page.total_sum()
        assert total == '58.29'

    browser.quit()