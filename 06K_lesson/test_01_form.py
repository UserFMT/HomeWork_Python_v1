import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get(" https://bonigarcia.dev/selenium-webdriver-java/data-types.html")


waiter =(WebDriverWait(driver).
         until(EC.visibility_of_element_located((By.NAME, "first-name"))))
(driver.find_element(
    By.CSS_SELECTOR, "input.form-control[name='first-name']").
    send_keys("Иван"))
(driver.find_element(
    By.CSS_SELECTOR, "input.form-control[name='last-name']").
    send_keys("Петров"))
(driver.find_element(
    By.CSS_SELECTOR, "input.form-control[name='address']").
    send_keys("Ленина, 55-3"))
(driver.find_element(
    By.CSS_SELECTOR, "input.form-control[name='e-mail']").
    send_keys("test@skypro.com"))
(driver.find_element(
    By.CSS_SELECTOR, "input.form-control[name='phone']").
    send_keys("+7985899998787"))
(driver.find_element(
    By.CSS_SELECTOR, "input.form-control[name='city']").
    send_keys("Москва"))
(driver.find_element(
    By.CSS_SELECTOR, "input.form-control[name='country']").
    send_keys("Россия"))
(driver.find_element(
    By.CSS_SELECTOR, "input.form-control[name='job-position']").
    send_keys("QA"))
(driver.find_element(
    By.CSS_SELECTOR, "input.form-control[name='company']").
    send_keys("SkyPro"))

driver.find_element(By.CLASS_NAME, "btn.btn-outline-primary.mt-3").click()

zip_code_attribute = (driver.find_element(By.ID, "zip-code").
                      value_of_css_property("background-color"))

all_elements = (driver.find_elements(By.CLASS_NAME, "alert.py-2"))


@pytest.mark.parametrize('txt, res', [
                         (zip_code_attribute, 'rgba(248, 215, 218, 1)')])
def test_zip_code_red(txt, res):
    assert txt == res


@pytest.mark.parametrize('all_elements, res', [
    (all_elements, 'rgba(209, 231, 221, 1)')])
def test_all_element_green(all_elements, res):
    all_color = True
    for element in all_elements:
        if (element.get_attribute("id") != 'zip-code' and
                element.value_of_css_property("background-color") !=
                'rgba(209, 231, 221, 1)'):
            all_color = False
    assert all_color is True

