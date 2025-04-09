import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver = webdriver.Firefox()
driver.get(url)
driver.implicitly_wait(10)
user ="Admin"
passs ="admin123"
driver.maximize_window()
time.sleep(1)
driver.find_element(By.XPATH,'//input[@placeholder="Username"]').click()
time.sleep(5)
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//input[@placeholder="Username"]').send_keys(user)
time.sleep(5)

driver.find_element(By.XPATH,'//input[@placeholder="Password"]').click()
driver.implicitly_wait(5)
time.sleep(5)
driver.find_element(By.XPATH,'//input[@placeholder="Password"]').send_keys(passs)
time.sleep(5)
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
time.sleep(100)