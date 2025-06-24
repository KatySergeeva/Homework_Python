from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")


username_input = driver.find_element(By.ID, 'username')
username_input.send_keys("tomsmith", Keys.RETURN)

password_input = driver.find_element(By.ID, 'password')
password_input.send_keys("SuperSecretPassword!")

sleep(5)

login_input = driver.find_element(By.XPATH, '//button[@type="submit"]')
login_input.click()
sleep(5)

driver.quit()