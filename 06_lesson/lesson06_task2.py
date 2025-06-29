from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(15)
driver.get("http://uitestingplayground.com/textinput")

search_input = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
search_input.send_keys("SkyPro")

blue_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
blue_button.click()

print(driver.find_element(By.CSS_SELECTOR, "#updatingButton").text)

driver.quit()