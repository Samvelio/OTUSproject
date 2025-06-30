import pytest
import allure
from ui.pages.login_page import LoginPage
from ui.pages.inventory_page import InventoryPage
from config.ui_config import UIConfig


@allure.feature("Cart")
class TestCart:
    @allure.title("Add product to cart")
    def test_add_product_to_cart(self, browser):
        browser.get("https://www.saucedemo.com")
        login_page = LoginPage(browser)
        login_page.login(UIConfig.VALID_USERNAME, UIConfig.VALID_PASSWORD)

        inventory_page = InventoryPage(browser)
        inventory_page.add_first_product_to_cart()
        assert inventory_page.get_cart_count() == 1

    @allure.title("Remove product from cart")
    def test_remove_product_from_cart(self, browser):
        browser.get("https://www.saucedemo.com")
        login_page = LoginPage(browser)
        login_page.login(UIConfig.VALID_USERNAME, UIConfig.VALID_PASSWORD)

        inventory_page = InventoryPage(browser)
        inventory_page.add_first_product_to_cart()
        inventory_page.add_first_product_to_cart()
        assert inventory_page.get_cart_count() == 0
