import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver


class FormPage:

    @allure.step("FormPage.init().Инициализация браузера")
    def __init__(self, driver: WebDriver, URL: str) -> None:
        self._driver = driver
        self._driver.get(URL)
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("FormPage.init_fields()."
                 "Заполнение полей формы данными {fields}")
    def init_fields(self, fields: dict[str]) -> None:
        for field_name, field_value in fields.items():
            (self._driver.find_element(
                By.CSS_SELECTOR, f"input.form-control[name='{field_name}']").
             send_keys(field_value))

    @allure.step("FormPage.button_click()."
                 "Нажатие кнопок из списка {button_name}")
    def button_click(self, button_name: dict[str]) -> None:
        self._driver.find_element(By.CLASS_NAME, button_name).click()

    @allure.step("FormPage.color_definition_field(). "
                 "Проверка соответствия цвета для поля {ID_field}")
    def color_definition_field(self, ID_field: str, color: str) -> bool:
        if (self._driver.find_element(By.ID, f"{ID_field}").
                value_of_css_property("background-color") == color):
            return True
        return False

    @allure.step("FormPage.color_definition_fields()."
                 "Проверка корректности цветов всех полей формы")
    def color_definition_fields(self,
                                fields: dict[str],
                                color: str) -> bool:
        all_color = True
        for field_name, field_value in fields.items():
            if (field_name != 'zip-code' and
                    self.color_definition_field(field_name, color)
                    is not True):
                all_color = False
        return all_color
