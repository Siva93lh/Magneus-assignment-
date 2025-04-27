
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://magnus.jalatechnologies.com/Home/Links")
driver.maximize_window()
time.sleep(2)

link1 = driver.find_element(By.LINK_TEXT, "Link 1")
print("Link 1 href:", link1.get_attribute("href"))

time.sleep(2)
driver.quit()
