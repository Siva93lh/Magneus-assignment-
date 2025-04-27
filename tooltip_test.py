
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://magnus.jalatechnologies.com/Home/Tooltip")
driver.maximize_window()
time.sleep(2)

tooltip = driver.find_element(By.XPATH, "//button[contains(text(),'Check the Tooltip Before You Click.')]")
print("Tooltip Text:", tooltip.get_attribute("title"))

time.sleep(2)
driver.quit()
