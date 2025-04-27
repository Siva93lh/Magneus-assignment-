
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://magnus.jalatechnologies.com/Home/Popup")
driver.maximize_window()
time.sleep(2)

popup_button = driver.find_element(By.XPATH, "//button[contains(text(),'Popup One')]")
popup_button.click()
time.sleep(2)
driver.quit()
