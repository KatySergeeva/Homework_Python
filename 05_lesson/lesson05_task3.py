from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")


input = driver.find_element(By.XPATH, '//input[@type="number"]')
input.send_keys("Sky", Keys.RETURN)

sleep(5)

input.clear()

input.send_keys("Pro", Keys.RETURN)

driver.quit()