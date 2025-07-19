from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    yield driver

@pytest.mark.usefixtures("driver")
def test_shopping(driver):
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # Авторизация
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Добавление товаров в корзину
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.refresh()

    # Переход в корзину и нажатие "Chekout"
    driver.find_element(By.ID, "shopping_cart_container").click()

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element(By.ID, "checkout").click()

    # Заполнение данных покупателя и нажатие "Continue"
    driver.find_element(By.ID, "first-name").send_keys("Екатерина")
    driver.find_element(By.ID, "last-name").send_keys("Сергеева")
    driver.find_element(By.ID, "postal-code").send_keys("443543")

    driver.find_element(By.ID, "continue").click()

    # Получение итоговой стоимости (Total)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    total = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
    clean_total = total.replace('Total: ', '').strip()
    driver.quit()
    assert clean_total == '$58.29'
