from selenium.webdriver.common.by import By


class FormPage:

    def __init__(self, driver, URL):
        self._driver = driver
        self._driver.get(URL)
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def init_fields(self, fields):
        for field_name, field_value in fields.items():
            (self._driver.find_element(
                By.CSS_SELECTOR, f"input.form-control[name='{field_name}']").
             send_keys(field_value))

    def button_click(self, button_name):
        self._driver.find_element(By.CLASS_NAME, button_name).click()

    def color_definition_field(self, ID_field, color):
        if (self._driver.find_element(By.ID, f"{ID_field}").
                value_of_css_property("background-color") == color):
            return True
        return False

    def color_definition_fields(self, fields, color):
        all_color = True
        for field_name, field_value in fields.items():
            if (field_name != 'zip-code' and
                    self.color_definition_field(field_name, color)
                    is not True):
                all_color = False
        return all_color
