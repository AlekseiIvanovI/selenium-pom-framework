from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.header_page import HeaderPage


class ProductPage(BasePage):
    PRODUCT_TITLE = (By.CLASS_NAME, "inventory_details_name.large_size")
    PRODUCT_DESC = (By.CLASS_NAME, "inventory_details_desc.large_size")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_details_price")

    def __init__(self, driver):
        super().__init__(driver)
        self.header = HeaderPage(driver)

    def get_product_title(self) -> str:
        element = self.wait.until(EC.visibility_of_element_located(self.PRODUCT_TITLE))
        return element.text.strip()

    def get_product_description(self) -> str:
        element = self.wait.until(EC.visibility_of_element_located(self.PRODUCT_DESC))
        return element.text.strip()

    def logout(self):
        self.header.logout()