# Откройте сайт магазина: https://www.saucedemo.com/.
# Авторизуйтесь как пользователь standard_user.
# Добавьте в корзину товары:
#  Sauce Labs Backpack.
#  Sauce Labs Bolt T-Shirt.
#  Sauce Labs Onesie.
# Перейдите в корзину.
# Нажмите Checkout.
# Заполните форму своими данными:
#  имя,
#  фамилия,
#  почтовый индекс.
# Нажмите кнопку Continue.
# Прочитайте со страницы итоговую стоимость ( Total ).
# Закройте браузер.
# Проверьте, что итоговая сумма равна $58.29.

import pytest

from selenium import webdriver

# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

model = ['Sauce Labs Backpack', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Onesie']
FIO = ['Иван', 'Иванов', '650400']
test_summa = '$58.29'

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")

(driver.find_element(By.CSS_SELECTOR, "[placeholder='Username']").
 send_keys('standard_user'))
(driver.find_element(By.CSS_SELECTOR, "[placeholder='Password']").
 send_keys('secret_sauce'))
driver.find_element(By.CLASS_NAME, "submit-button.btn_action").click()

elements = driver.find_elements(By.CLASS_NAME, 'inventory_item')
for element in elements:
    if (element.find_element(
            By.CLASS_NAME, "inventory_item_name").text in model):
        (element.find_element(
            By.CLASS_NAME, "btn.btn_primary.btn_small.btn_inventory ").
         click())


waiter = WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located(
        (By.CLASS_NAME, 'shopping_cart_badge')))
driver.find_element(
    By.CLASS_NAME, 'shopping_cart_link').click()
driver.find_element(
    By.CLASS_NAME, 'btn.btn_action.btn_medium.checkout_button').click()

elements = driver.find_elements(By.CLASS_NAME, 'form_group')
for element in elements:
    if (element.find_element(
           By.CLASS_NAME, 'input_error.form_input').
            get_attribute("placeholder")) == 'First Name':
        (element.find_element(By.CLASS_NAME, 'input_error.form_input').
         send_keys(FIO[0]))
    elif (element.find_element(
           By.CLASS_NAME,
           'input_error.form_input').
            get_attribute("placeholder")) == 'Last Name':
        (element.find_element(By.CLASS_NAME, 'input_error.form_input').
         send_keys(FIO[1]))
    elif ((element.find_element(
           By.CSS_SELECTOR,
           'input.input_error.form_input').get_attribute("placeholder")) ==
          'Zip/Postal Code'):
        (element.find_element(By.CLASS_NAME, 'input_error.form_input').
         send_keys(FIO[2]))
(driver.find_element(
    By.CLASS_NAME, 'submit-button.btn.btn_primary.cart_button.btn_action').
    click())

waiter = WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located(
        (By.CLASS_NAME, 'summary_total_label')))
total = driver.find_element(By.CLASS_NAME, 'summary_total_label').text[7:]

driver.quit()


@pytest.mark.parametrize('summa, result', [(total, test_summa)])
def test_total_summa(summa, result):
    assert summa == result
