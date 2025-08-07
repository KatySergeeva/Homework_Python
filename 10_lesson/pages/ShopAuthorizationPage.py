from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


class ShopAuthorizationPage:
    """
    Класс для авторизации покупателя
    """
    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()

    def authorization(self):
        """
        Открываем страницу интернет-магазина и вводим логин/пароль для авторизации
        """
        self._driver.get("https://www.saucedemo.com/")
        username = self._driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")

        password = self._driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")
        self._driver.find_element(By.ID, "login-button").click()
    
