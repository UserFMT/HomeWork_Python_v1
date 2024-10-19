import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

time_delay = 45

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/"
           "slow-calculator.html")

driver.find_element(By.CSS_SELECTOR, "#delay").clear()
driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(f'{time_delay}')
driver.find_element(By.XPATH, "//span[text()='7']").click()
driver.find_element(By.XPATH, "//span[text()='+']").click()
driver.find_element(By.XPATH, "//span[text()='8']").click()
driver.find_element(By.XPATH, "//span[text()='=']").click()

waiter = WebDriverWait(driver, time_delay+1).until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, 'div.screen'), '15'))
text = driver.find_element(By.CSS_SELECTOR, 'div.screen').text

driver.quit()


@pytest.mark.parametrize('text, result', [(text, "15")])
def test_result_waiter(text, result):
    assert text == result
