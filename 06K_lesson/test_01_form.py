from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.implicitly_wait(30)
    yield driver


@pytest.mark.usefixtures("driver")
def test_form(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    first_name = driver.find_element(By.XPATH, '//input[@name="first-name"]')
    first_name.send_keys("Иван")

    last_name = driver.find_element(By.XPATH, '//input[@name="last-name"]')
    last_name.send_keys("Петров")

    address = driver.find_element(By.XPATH, '//input[@name="address"]')
    address.send_keys("Ленина, 55-3")

    email = driver.find_element(By.XPATH, '//input[@name="e-mail"]')
    email.send_keys("test@skypro.com")

    phone = driver.find_element(By.XPATH, '//input[@name="phone"]')
    phone.send_keys("+7985899998787")

    zip = driver.find_element(By.XPATH, '//input[@name="zip-code"]')
    zip.send_keys("")

    city = driver.find_element(By.XPATH, '//input[@name="city"]')
    city.send_keys("Москва")

    country = driver.find_element(By.XPATH, '//input[@name="country"]')
    country.send_keys("Россия")

    job_position = driver.find_element(By.XPATH, '//input[@name="job-position"]')
    job_position.send_keys("QA")

    company = driver.find_element(By.XPATH, '//input[@name="company"]')
    company.send_keys("SkyPro")

    button_submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
    button_submit.click()

    color_zip = driver.find_element(By.ID, "zip-code").get_attribute("class")
    assert color_zip == "alert py-2 alert-danger"

    rest_fields_color = ["#first-name", "#last-name", "#address", "#city", "#country", "#e-mail", "#phone", "#company"]
    for field in rest_fields_color:
        pole_class = driver.find_element(By.CSS_SELECTOR, field).get_attribute("class")
        assert pole_class == "alert py-2 alert-success"

    driver.quit()
