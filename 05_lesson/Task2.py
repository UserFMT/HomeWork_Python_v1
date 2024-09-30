from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

# Откройте страницу http://uitestingplayground.com/dynamicid.
driver.get("http://uitestingplayground.com/dynamicid")

# driver.maximize_window()
# Запуск скрипта 3 раза
for i in range(3):
    driver.refresh()
    # Ждем, пока кнопка синего цвета станет кликабельной
    blue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    "button.btn.btn-primary")))

    # Кликните на синюю кнопку.
    blue_button = driver.find_element(By.CSS_SELECTOR,
                                      "button.btn.btn-primary").click()

sleep(2)

driver.quit()
