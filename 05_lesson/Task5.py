from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.firefox.service import Service as FirefoxService

driver = webdriver.Firefox()

# Откройте страницу http://the-internet.herokuapp.com/inputs.
driver.get('http://the-internet.herokuapp.com/inputs')
sleep(2)
# Введите в поле текст  1000.
input_number = driver.find_element(By.CSS_SELECTOR,
                                   "input[type='number']").send_keys("1000")
sleep(2)

# Очистите это поле (метод clear).
input_number = driver.find_element(By.CSS_SELECTOR,
                                   "input[type='number']").clear()
sleep(2)

# Введите в это же поле текст 999.
input_number = driver.find_element(By.CSS_SELECTOR,
                                   "input[type='number']").send_keys("999")
sleep(2)

driver.quit()
