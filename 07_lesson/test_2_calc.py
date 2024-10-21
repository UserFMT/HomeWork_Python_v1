import pytest

from selenium import webdriver
from CalcPage import CalcPage


URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
time_delay = 45
collection_symbol = ['7', '+', '8', '=']
result = 15
selector = ['#delay', 'div.screen']

browser = webdriver.Chrome()
calc_page = CalcPage(browser, URL)
calc_page.input_field(selector[0], time_delay)
calc_page.click_button(collection_symbol)
text = calc_page.waiting_result(selector[0], str(result), selector[1])


@pytest.mark.parametrize('text, result', [(text, str(result))])
def test_result(text, result):
    assert text == result


browser.quit()
