from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
    )

# Откройте страницу
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Пять раз кликните на кнопку Add Element
for i in range(5):
    add_Button = (driver.find_element(
        By.CSS_SELECTOR,
        "button[onclick='addElement()']").click())
sleep(1)

# Соберите со страницы список кнопок Delete
result_button_delete = driver.find_elements(
    By.CSS_SELECTOR, "button[onclick='deleteElement()']")

# Выведите на экран размер списка
print(f'Количество кнопок DELETE - {len(result_button_delete)} ')

sleep(2)

driver.quit()
