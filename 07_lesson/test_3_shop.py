import pytest

from selenium import webdriver
from ShopPage import ShopPage


URL = "https://www.saucedemo.com"
field_init = {
    "Username": "standard_user",
    "Password": "secret_sauce"
}
model = ['Sauce Labs Backpack',
         'Sauce Labs Bolt T-Shirt',
         'Sauce Labs Onesie'
         ]
FIO = {
    'first-name': 'Иван',
    'last-name': 'Иванов',
    'postal-code': '650400'
}
test_summa = '$58.29'
selector_init_user = "submit-button.btn_action"
selector_options = ["inventory_item",
                    "inventory_item_name",
                    "btn.btn_primary.btn_small.btn_inventory"
                    ]
selector_cart = ["shopping_cart_badge",
                 "shopping_cart_link",
                 "btn.btn_action.btn_medium.checkout_button"
                 ]
selector_user = 'submit-button.btn.btn_primary.cart_button.btn_action'
selector_result = 'summary_total_label'


browser = webdriver.Chrome()
shop_page = ShopPage(browser, URL)
shop_page.init_user(field_init, selector_init_user)
shop_page.product_selection(selector_options[0], selector_options[1],
                            selector_options[2], model)
shop_page.go_cart(selector_cart[0], selector_cart[1], selector_cart[2])
shop_page.user_fileds(FIO, selector_user)
total = shop_page.total_summ(selector_result)


@pytest.mark.parametrize('summa, result', [(total, test_summa)])
def test_total_summa(summa, result):
    assert summa == result


browser.quit()
