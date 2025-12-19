from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "title")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    CHECKOUT = (By.ID, "checkout")

    def get_page_title(self) -> str:
        return self.text_of(self.PAGE_TITLE)

    def is_item_in_cart(self, item_name="Sauce Labs Backpack") -> bool:
        items = self.driver.find_elements(*self.ITEM_NAME)
        return any(item.text == item_name for item in items)

    def remove_backpack(self):
        self.click(self.REMOVE_BUTTON)

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING)

    def checkout(self):
        self.click(self.CHECKOUT)