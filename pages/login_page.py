from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    USER_NAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")

    def load(self, base_url: str):
        self.open(base_url)

    def login(self, user_name: str, password: str):
        self.type(self.USER_NAME, user_name)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def get_error_message(self):
        return self.text_of(self.ERROR_MESSAGE)