import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:

    @allure.step("CalcPage.init(). Инициализация страницы ")
    def __init__(self, driver: WebDriver, URL: str) -> None:
        self._driver = driver
        self._driver.get(URL)
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("CalcPage.input_field(). "
                 "Фиксация времени ожидания в секундах : {time_delay}")
    def input_field(self, selector: str, time_delay: int) -> None:
        self._driver.find_element(By.CSS_SELECTOR, selector).clear()
        (self._driver.find_element(By.CSS_SELECTOR, selector).
         send_keys(f'{time_delay}'))

    @allure.step("CalcPage.click_button(). "
                 "Нажатие кнопок калькулятора. "
                 "Кнопки определены в параметре collection")
    def click_button(self, collection: list[str]) -> None:
        for symbol in collection:
            (self._driver.find_element(By.XPATH, f"//span[text()='{symbol}']").
             click())

    @allure.step("CalcPage.waiting_result(). "
                 "Ожидание результатов вычислений")
    def waiting_result(self, selector_delay: str,
                       result: str,
                       selector: str) -> str:
        time_delay = int(self._driver.find_element(
            By.CSS_SELECTOR, selector_delay).get_attribute("value"))+1
        WebDriverWait(self._driver, time_delay).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, selector), result))
        return self._driver.find_element(By.CSS_SELECTOR, selector).text
