import allure

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


@allure.epic("Форма с данными пользователя")
@allure.description("Тестирование сайта заказа одежды")
@allure.severity("critical")
def test_form_user():
    with allure.step("Открываем страницу браузера"):
        browser = webdriver.Chrome()
        form_page = FormPage(browser, URL)

    with allure.step("Работаем с формой ввода: "):
        form_page.init_fields(fields)
        form_page.button_click(button_name)

    with allure.step("Проверка цвета для одного поля формы : "):
        color_fields = form_page.color_definition_field("zip-code", color_red)
        assert color_fields is True

    with allure.step("Проверка цветов для остальных полей формы : "):
        color_fields = form_page.color_definition_fields(fields, color_green)
        assert color_fields is True

    with allure.step("Закрытие сессии браузера."):
        browser.quit()
