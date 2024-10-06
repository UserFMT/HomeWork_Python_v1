# from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

# Перейдите на сайт
# https://bonigarcia.dev/selenium-webdriver-java/loading-images.html.
driver.get("https://bonigarcia.dev/"
           "selenium-webdriver-java/loading-images.html")


# Дождитесь загрузки всех картинок.
# (<div class="col-12 py-2" id="image-container">+рекомендации наставников
waiter = WebDriverWait(driver, 40)
waiter.until(EC.presence_of_all_elements_located(
    (By.CSS_SELECTOR,
     'div#image-container.col-12.py-2 img#landscape')))

# Получите значение атрибута  src  у 3-й картинки.
imgs = driver.find_elements(By.CSS_SELECTOR,
                            'div#image-container.col-12.py-2 img')
img_src = imgs[2]

# Выведите значение в консоль.
print(img_src.get_attribute('src'))

driver.quit()
