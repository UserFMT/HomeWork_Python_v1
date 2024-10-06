# from time import sleep
from selenium import webdriver

# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Перейдите на сайт http://uitestingplayground.com/textinput.
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

# Укажите в поле ввода текст SkyPro.
# <input class="form-control" type="text"
# placeholder="MyButton" id="newButtonName">
input = driver.find_element(By.CSS_SELECTOR,
                            '#newButtonName').send_keys("SkyPro")

# Нажмите на синюю кнопку.
# <button class="btn btn-primary" type="button"
# id="updatingButton">Button That Should Change it's Name Based
# on Input Value</button>
driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()

# Получите текст кнопки и выведите в консоль ("SkyPro").

waiter = WebDriverWait(driver, 10)
waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,
                                               '#updatingButton'), 'SkyPro'))

button = driver.find_element(By.CSS_SELECTOR, '#updatingButton')

print(button.text)
driver.quit()
