import pytest
import allure
from selenium import webdriver
from CalcPage import CalcPage


URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
time_delay = 45
collection_symbol = ['7', '+', '8', '=']
result = 15
selector = ['#delay', 'div.screen']


@allure.epic("Калькулятор")
@allure.description("Тестирование сайта онлайн-калькулятора")
@allure.severity("critical")
@pytest.mark.parametrize('result_test', [(str(result))])
def test_calculator(result_test):
    with allure.step("Открываем страницу браузера"):
        browser = webdriver.Chrome()
        calc_page = CalcPage(browser, URL)

    with allure.step("Работаем с формой  калькулятором: "):
        calc_page.input_field(selector[0], time_delay)
        calc_page.click_button(collection_symbol)

    with allure.step("Проверка итогов расчета."):
        text = calc_page.waiting_result(selector[0], str(result), selector[1])
        assert text == result_test

    with allure.step("Закрытие сессии браузера."):
        browser.quit()
