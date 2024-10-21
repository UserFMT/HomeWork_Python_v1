import pytest

from FormPage import FormPage
from selenium import webdriver

URL = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

fields = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "zip-code": "",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }
button_name = 'btn.btn-outline-primary.mt-3'
color_green = 'rgba(209, 231, 221, 1)'
color_red = 'rgba(248, 215, 218, 1)'

browser = webdriver.Chrome()
form_page = FormPage(browser, URL)
form_page.init_fields(fields)
form_page.button_click(button_name)


color_fields = form_page.color_definition_field(
    "zip-code", color_red)


@pytest.mark.parametrize('param', [color_fields])
def test_field(param):
    assert param is True


color_fields = form_page.color_definition_fields(fields, color_green)


@pytest.mark.parametrize('param', [color_fields])
def test_fields(param):
    assert param is True


browser.quit()
