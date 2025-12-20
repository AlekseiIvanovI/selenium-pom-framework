from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class HeaderPage(BasePage):
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def open_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.BURGER_MENU)).click()

    def logout(self):
        self.open_menu()
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_LINK)).click()

    def get_cart_count(self) -> int:
        if self.isvisible(self.CART_BADGE):
            return int(self.text_of(self.CART_BADGE))
        return 0

    def go_to_cart(self):
        self.click(self.CART_LINK)