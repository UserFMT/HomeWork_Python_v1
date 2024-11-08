import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sqlalchemy.dialects.postgresql import array


class ShopPage:

    @allure.step("ShopPage.init(). Инициализация браузера")
    def __init__(self, driver: WebDriver, URL: str) -> None:
        self._driver = driver
        self._driver.get(URL)
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("ShopPage.init_user(). Инициализация пользователя")
    def init_user(self, fields: dict[str], selector: str) -> None:
        for field_name, field_value in fields.items():
            (self._driver.find_element(
                By.CSS_SELECTOR, f"[placeholder='{field_name}']").
             send_keys(field_value))
        self._driver.find_element(By.CLASS_NAME, selector).click()

    @allure.step("ShopPage.product_selection(). "
                 "Выбор моделей одежды для заказа")
    def product_selection(self, selector_1: str,
                          selector_2: str,
                          selector_3: str,
                          model: array[str]) -> None:
        elements = self._driver.find_elements(By.CLASS_NAME, selector_1)
        for element in elements:
            if (element.find_element(By.CLASS_NAME, selector_2).
                    text in model):
                (element.find_element(By.CLASS_NAME, selector_3).click())

    @allure.step("ShopPage.go_cart(). Переход в корзину пользователя")
    def go_cart(self, selector_1: str,
                selector_2: str,
                selector_3: str) -> None:
        (WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.CLASS_NAME, selector_1))))
        self._driver.find_element(By.CLASS_NAME, selector_2).click()
        self._driver.find_element(By.CLASS_NAME, selector_3).click()

    @allure.step("ShopPage.user_fileds(). Ввод данных о пользователе")
    def user_fileds(self, FIO: dict, selector: str) -> None:
        for field_name, field_value in FIO.items():
            (self._driver.find_element(By.ID, field_name).
             send_keys(field_value))
        self._driver.find_element(By.CLASS_NAME, selector).click()

    @allure.step("ShopPage.total_summ(). Определение итоговой суммы заказа")
    def total_summ(self, selector: str) -> str:
        WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.CLASS_NAME, selector)))
        return self._driver.find_element(By.CLASS_NAME, selector).text[7:]
