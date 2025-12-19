import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from screenshoot_utility import take_screenshot

load_dotenv()

@pytest.fixture(scope="function")
def driver():
    # Disable password manager prompts for cleaner automation
    chrome_options = Options()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    chrome_options.add_experimental_option("prefs", prefs)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def base_url():
    return os.getenv("BASE_URL", "https://www.saucedemo.com/")

@pytest.fixture()
def credentials():
    return {
        "user_name": os.getenv("USER_NAME", "standard_user"),
        "password": os.getenv("PASSWORD", "secret_sauce")
    }
# Automatically take a screenshot when a test fails
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            take_screenshot(driver, f"FAILED_{item.name}.png")