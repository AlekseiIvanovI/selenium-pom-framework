import os
import time

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from screenshoot_utility import take_screenshot

load_dotenv()

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    options.add_experimental_option("prefs", prefs)

    if os.getenv("GITHUB_ACTIONS") or os.getenv("DOCKER"):
        command_executor = "http://localhost:4444/wd/hub"
    else:
        command_executor = "http://chrome:4444/wd/hub"

    driver = webdriver.Remote(
        command_executor=command_executor,
        options=options
    )
    driver.maximize_window()

    driver.wait = WebDriverWait(driver, 15)

    yield driver
    driver.quit()

# @pytest.fixture(scope="function")
# def driver():
#     # Disable password manager prompts for cleaner automation
#     chrome_options = Options()
#     prefs = {
#         "credentials_enable_service": False,
#         "profile.password_manager_enabled": False,
#         "profile.password_manager_leak_detection": False
#     }
#     chrome_options.add_experimental_option("prefs", prefs)
#
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=chrome_options)
#     driver.maximize_window()
#     driver.wait = WebDriverWait(driver, 10)
#     yield driver
#     driver.quit()

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