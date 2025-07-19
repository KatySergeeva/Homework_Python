from selenium import webdriver
import pytest
from pages.ShopAuthorizationPage import ShopAuthorizationPage
from pages.ShopMainPage import ShopMainPage
from pages.ShopCardPage import ShopCardPage
from pages.ShopOrderPage import ShopOrderPage


def test_shop():
    browser = webdriver.Firefox()

    authorization_page = ShopAuthorizationPage(browser)
    authorization_page.authorization()

    main_page = ShopMainPage(browser)
    main_page.add_card()
    main_page.go_to_card()

    card_page = ShopCardPage(browser)
    card_page.checkout()

    order_page = ShopOrderPage(browser)
    order_page.data_registration()

    total = order_page.total_sum()
    assert total == '58.29'

    browser.quit()
