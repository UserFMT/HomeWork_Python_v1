from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

# Откройте страницу http://uitestingplayground.com/classattr.
driver.get("http://uitestingplayground.com/classattr")

# Кликните на синюю кнопку.
# Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково.
# (Решила так попробовать сделать)
for i in range(3):
    blue_button = (driver.find_element(
        By.XPATH,
        "//button[contains(concat(' ', normalize-space(@class),' '), "
        "' btn-primary ')]").click())
    sleep(5)
    driver.refresh()

driver.quit()
