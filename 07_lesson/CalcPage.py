from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:

    def __init__(self, driver, URL):
        self._driver = driver
        self._driver.get(URL)
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def input_field(self, selector, time_delay):
        self._driver.find_element(By.CSS_SELECTOR, selector).clear()
        (self._driver.find_element(By.CSS_SELECTOR, selector).
         send_keys(f'{time_delay}'))

    def click_button(self, collection):
        for symbol in collection:
            (self._driver.find_element(By.XPATH, f"//span[text()='{symbol}']").
             click())

    def waiting_result(self, selector_delay, result, selector):
        time_delay = int(self._driver.find_element(
            By.CSS_SELECTOR, selector_delay).get_attribute("value"))+1
        WebDriverWait(self._driver, time_delay).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, selector), result))
        return self._driver.find_element(By.CSS_SELECTOR, selector).text

    def print_error(self):
        return "Итог теста невалидный"
