from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class InventoryPage(BasePage):
    ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    BACKPACK_LINK = (By.ID, "item_4_title_link")

    def add_to_cart_backpack(self):
        self.click(self.ADD_TO_CART_BACKPACK)

    def get_cart_item_count(self) -> int:
        if self.isvisible(self.CART_BADGE):
            return int(self.text_of(self.CART_BADGE))
        return 0

    def go_to_cart_page(self):
        self.click(self.CART_LINK)

    def sort_items_za(self):
        sort_element = self.wait.until(EC.element_to_be_clickable(self.SORT_DROPDOWN))
        select = Select(sort_element)
        select.select_by_value("za")

    def go_to_backpack_page(self):
        self.click(self.BACKPACK_LINK)

    def sort_items_az(self):
        select = Select(self.wait.until(EC.element_to_be_clickable(self.SORT_DROPDOWN)))
        select.select_by_value("az")

    def sort_by_price_low_to_high(self):
        select = Select(self.wait.until(EC.element_to_be_clickable(self.SORT_DROPDOWN)))
        select.select_by_value("lohi")

    def add_to_cart_bike_light(self):
        self.click((By.ID, "add-to-cart-sauce-labs-bike-light"))

    def add_to_cart_tshirt(self):
        self.click((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))

    def get_all_product_titles(self):
        elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [e.text for e in elements]

    def get_all_product_prices(self):
        elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        return [float(e.text.replace("$", "")) for e in elements]