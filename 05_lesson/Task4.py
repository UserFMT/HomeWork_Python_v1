from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()

# Откройте страницу http://the-internet.herokuapp.com/entry_ad.
driver.get('http://the-internet.herokuapp.com/entry_ad')
sleep(2)

# В модальном окне нажмите на кнопку Сlose

# Ждем, пока  кнопка модального окна станет кликабельной
button_close = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div.modal")))

# Нажимаем кнопку
driver.find_element(By.CSS_SELECTOR, "div.modal-footer").click()

print("Кнопка нажата! Окно драйвера закрыто.")

driver.quit()
