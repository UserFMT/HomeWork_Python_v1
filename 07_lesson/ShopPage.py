from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:

    def __init__(self, driver, URL):
        self._driver = driver
        self._driver.get(URL)
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def init_user(self, fields, selector):
        for field_name, field_value in fields.items():
            (self._driver.find_element(
                By.CSS_SELECTOR, f"[placeholder='{field_name}']").
             send_keys(field_value))
        self._driver.find_element(By.CLASS_NAME, selector).click()

    def product_selection(self, selector_1, selector_2, selector_3, model):
        elements = self._driver.find_elements(By.CLASS_NAME, selector_1)
        for element in elements:
            if (element.find_element(By.CLASS_NAME, selector_2).
                    text in model):
                (element.find_element(By.CLASS_NAME, selector_3).click())

    def go_cart(self, selector_1, selector_2, selector_3):
        (WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.CLASS_NAME, selector_1))))
        self._driver.find_element(By.CLASS_NAME, selector_2).click()
        self._driver.find_element(By.CLASS_NAME, selector_3).click()

    def user_fileds(self, FIO, selector):
        for field_name, field_value in FIO.items():
            (self._driver.find_element(By.ID, field_name).
             send_keys(field_value))
        self._driver.find_element(By.CLASS_NAME, selector).click()

    def total_summ(self, selector):
        WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.CLASS_NAME, selector)))
        return self._driver.find_element(By.CLASS_NAME, selector).text[7:]
