from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.header_page import HeaderPage


class CheckoutPage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "title")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)
        self.header = HeaderPage(driver)

    def get_page_title(self) -> str:
        return self.text_of(self.PAGE_TITLE)

    def fill_information(self, first_name, last_name, zip_code):
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.ZIP_CODE, zip_code)
        self.click(self.CONTINUE_BUTTON)

    def get_error_message(self) -> str:
        if self.isvisible(self.ERROR_MESSAGE):
            return self.text_of(self.ERROR_MESSAGE)
        return ""

    CANCEL_BUTTON = (By.ID, "cancel")

    def cancel_checkout(self):
        self.click(self.CANCEL_BUTTON)

    def logout(self):
        self.header.logout()