# from time import sleep
from selenium import webdriver

# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# Перейдите на страницу http://uitestingplayground.com/ajax.
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")
driver.implicitly_wait(20)

# Нажмите на синюю кнопку.
# (<button class="btn btn-primary" type="button" id="ajaxButton"
# onclick="LoadLabel()">Button Triggering AJAX Request</button>)
driver.find_element(By.CSS_SELECTOR, '#ajaxButton').click()

# Получите текст из зеленой плашки. (id=content)
element = driver.find_element(By.CSS_SELECTOR, '#content')

# Выведите его в консоль
# ("Data loaded with AJAX get request.").
# (<p class="bg-success">Data loaded with AJAX get request.</p>)
print(element.find_element(By.CLASS_NAME, 'bg-success').text)

driver.quit()
