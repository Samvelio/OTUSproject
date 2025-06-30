import pytest
import allure
from ui.pages.login_page import LoginPage
from config.ui_config import UIConfig


@allure.feature("Login")
class TestLogin:
    @allure.title("Successful login")
    def test_successful_login(self, browser):
        browser.get("https://www.saucedemo.com")
        login_page = LoginPage(browser)
        login_page.login(UIConfig.VALID_USERNAME, UIConfig.VALID_PASSWORD)
        assert "inventory" in browser.current_url

    @allure.title("Locked user login")
    def test_locked_user_login(self, browser):
        browser.get("https://www.saucedemo.com")
        login_page = LoginPage(browser)
        login_page.login(UIConfig.LOCKED_USER, UIConfig.VALID_PASSWORD)
        assert "Epic sadface: Sorry, this user has been locked out" in login_page.get_error_message()

    @allure.title("Invalid credentials")
    @pytest.mark.parametrize("username, password", [
        ("invalid", UIConfig.VALID_PASSWORD),
        (UIConfig.VALID_USERNAME, "invalid"),
        ("", ""),
        (None, None)
    ])
    def test_invalid_credentials(self, browser, username, password):
        browser.get("https://www.saucedemo.com")
        login_page = LoginPage(browser)
        login_page.login(username, password)
        assert "Epic sadface: Username and password do not match" in login_page.get_error_message()
        