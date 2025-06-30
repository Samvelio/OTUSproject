from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from config.ui_config import UIConfig
import pytest
import os


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=UIConfig.BROWSER)
    parser.addoption("--headless", action="store_true", default=UIConfig.HEADLESS)


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser").lower()
    headless = request.config.getoption("--headless")

    if browser_name == "chrome":
        chrome_options = ChromeOptions()
        if os.path.exists("/opt/chrome-for-testing/chrome"):
            chrome_options.binary_location = "/opt/chrome-for-testing/chrome"
        if headless:
            chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(
            service=ChromeService(),
            options=chrome_options
        )

    elif browser_name == "firefox":
        firefox_options = FirefoxOptions()
        if headless:
            firefox_options.add_argument("--headless")

        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=firefox_options
        )
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    yield driver
    driver.quit()