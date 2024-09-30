from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

# Откройте страницу http://the-internet.herokuapp.com/login.
driver.get('http://the-internet.herokuapp.com/login')
sleep(2)

# В поле username введите значение tomsmith.
input_user = driver.find_element(By.ID, "username").send_keys("tomsmith")
sleep(2)

# В поле password введите значение SuperSecretPassword!.
input_password = (driver.find_element(By.ID, "password").
                  send_keys("SuperSecretPassword"))
sleep(2)

# Нажмите кнопку Login
button_login = driver.find_element(By.CLASS_NAME, "radius").click()

sleep(1)

driver.quit()
