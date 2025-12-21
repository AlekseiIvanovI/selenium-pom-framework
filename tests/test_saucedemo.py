from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.product_page import ProductPage

def login_and_get_pages(driver, base_url, credentials):
    #Helper: Logs in and returns initialized InventoryPage and CartPage objects.
        login_page = LoginPage(driver)
        login_page.load(base_url)
        login_page.login(credentials["user_name"], credentials["password"])
        assert "inventory.html" in driver.current_url, "Login failed"
        return InventoryPage(driver), CartPage(driver)

def test_login(driver, base_url, credentials):
    #Basic smoke test: verifies successful login redirects to inventory page.
        inventory_page, _ = login_and_get_pages(driver, base_url, credentials)

def test_product_page(driver, base_url, credentials):
    #Verify product description on the Backpack detail page.
        inventory_page, _ = login_and_get_pages(driver, base_url, credentials)
        inventory_page.go_to_backpack_page()

        product_page = ProductPage(driver)
        actual = product_page.get_product_description()
        expected = (
            "carry.allTheThings() with the sleek, streamlined Sly Pack that melds "
            "uncompromising style with unequaled laptop and tablet protection."
        )
        assert actual == expected, f"Description mismatch.\nGot: {actual}"

def test_add_to_cart_success(driver, base_url, credentials):
    #Add one item to cart and verify cart badge updates
        inventory_page, _ = login_and_get_pages(driver, base_url, credentials)
        assert inventory_page.get_cart_item_count() == 0, "Cart should start empty"
        inventory_page.add_to_cart_backpack()
        assert inventory_page.get_cart_item_count() == 1, "Cart should have 1 item"

def test_sort_items(driver, base_url, credentials):
    #Simple sort test (Z-A) – verification can be added later
        inventory_page, _ = login_and_get_pages(driver, base_url, credentials)
        inventory_page.sort_items_za()
        # Add verification later if needed

def test_add_to_cart_failure_screenshot(driver, base_url, credentials):
    #Intentionally failing test to demonstrate screenshot on failure
        inventory_page, _ = login_and_get_pages(driver, base_url, credentials)
        assert inventory_page.get_cart_item_count() == 0
        inventory_page.add_to_cart_backpack()
        assert inventory_page.get_cart_item_count() == 2, "INTENTIONAL FAILURE → triggers screenshot"

def test_remove_from_cart(driver, base_url, credentials):
    #Add item, go to cart, remove it, and verify cart is empty
        inventory_page, cart_page = login_and_get_pages(driver, base_url, credentials)

        inventory_page.add_to_cart_backpack()
        assert inventory_page.get_cart_item_count() == 1

        inventory_page.go_to_cart_page()
        assert "cart.html" in driver.current_url

        assert cart_page.get_page_title() == "Your Cart"
        assert cart_page.is_item_in_cart("Sauce Labs Backpack")

        cart_page.remove_backpack()
        assert not cart_page.is_item_in_cart("Sauce Labs Backpack")
        assert inventory_page.get_cart_item_count() == 0

def test_checkout(driver, base_url, credentials):
    #Partial checkout flow up to overview page
        inventory_page, cart_page = login_and_get_pages(driver, base_url, credentials)

        inventory_page.add_to_cart_backpack()
        assert inventory_page.get_cart_item_count() == 1

        inventory_page.go_to_cart_page()
        assert "cart.html" in driver.current_url
        assert cart_page.get_page_title() == "Your Cart"

        cart_page.checkout()
        assert "checkout-step-one.html" in driver.current_url

        checkout_page = CheckoutPage(driver)
        assert checkout_page.get_page_title() == "Checkout: Your Information"
        checkout_page.fill_information("John", "Doe", "90210")

        assert "checkout-step-two.html" in driver.current_url, "Should reach checkout overview"

def test_login_invalid_credentials(driver, base_url):
    #Negative test: invalid credentials should show error and stay on login page
    login_page = LoginPage(driver)
    login_page.load(base_url)
    login_page.login("wrong_user", "wrong_pass")


    assert "inventory.html" not in driver.current_url
    error = login_page.get_error_message()
    assert "Username and password do not match" in error


def test_sort_items_az(driver, base_url, credentials):
    #Verify sorting A → Z by product name
    inventory_page, _ = login_and_get_pages(driver, base_url, credentials)
    inventory_page.sort_items_az()

    titles = inventory_page.get_all_product_titles()
    assert titles == sorted(titles), "Items not sorted A to Z"
    assert titles[0] == "Sauce Labs Backpack", "First item should be Sauce Labs Backpack in A-Z"


def test_sort_items_za(driver, base_url, credentials):
    #Verify sorting Z → A by product name
    inventory_page, _ = login_and_get_pages(driver, base_url, credentials)
    inventory_page.sort_items_za()

    titles = inventory_page.get_all_product_titles()
    assert titles == sorted(titles, reverse=True), "Items not sorted Z to A"
    assert titles[0].startswith("Test.allTheThings()"), "First item should start with 'Test.allTheThings()' in Z-A"


def test_sort_price_low_to_high(driver, base_url, credentials):
    #Verify price sorting low → high
    inventory_page, _ = login_and_get_pages(driver, base_url, credentials)
    inventory_page.sort_by_price_low_to_high()

    prices = inventory_page.get_all_product_prices()
    assert prices == sorted(prices), "Prices not sorted low to high"
    assert prices[0] == 7.99, "Cheapest item should be $7.99"


def test_add_multiple_items_to_cart(driver, base_url, credentials):
    #Add three different items and verify they appear in cart
    inventory_page, _ = login_and_get_pages(driver, base_url, credentials)
    inventory_page.add_to_cart_backpack()
    inventory_page.add_to_cart_bike_light()
    inventory_page.add_to_cart_tshirt()

    assert inventory_page.get_cart_item_count() == 3
    inventory_page.go_to_cart_page()
    cart_page = CartPage(driver)
    assert cart_page.is_item_in_cart("Sauce Labs Backpack")
    assert cart_page.is_item_in_cart("Sauce Labs Bike Light")
    assert cart_page.is_item_in_cart("Sauce Labs Bolt T-Shirt")


def test_continue_shopping(driver, base_url, credentials):
    #From cart page, click Continue Shopping and return to inventory
    inventory_page, cart_page = login_and_get_pages(driver, base_url, credentials)
    inventory_page.add_to_cart_backpack()
    inventory_page.go_to_cart_page()

    cart_page.continue_shopping()
    assert "cart.html" not in driver.current_url
    assert "inventory.html" in driver.current_url
    assert inventory_page.get_cart_item_count() == 1


def test_checkout_cancel_from_overview(driver, base_url, credentials):
    #Cancel checkout from overview page and return to inventory
    inventory_page, cart_page = login_and_get_pages(driver, base_url, credentials)
    inventory_page.add_to_cart_backpack()
    inventory_page.go_to_cart_page()
    cart_page.checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_information("Jane", "Smith", "12345")

    overview_page = CheckoutPage(driver)
    overview_page.cancel_checkout()

    assert "inventory.html" in driver.current_url
    assert inventory_page.get_cart_item_count() == 1


def test_complete_checkout_flow(driver, base_url, credentials):
    #End-to-end: add item → checkout → fill info → finish → success page
    inventory_page, cart_page = login_and_get_pages(driver, base_url, credentials)
    inventory_page.add_to_cart_backpack()
    inventory_page.go_to_cart_page()
    cart_page.checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_information("Test", "User", "90210")

    # On overview – click Finish
    finish_button = driver.wait.until(EC.element_to_be_clickable((By.ID, "finish")))
    finish_button.click()


    assert "checkout-complete.html" in driver.current_url
    success_header = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert success_header == "Thank you for your order!"


def test_logout_inventory_page(driver, base_url, credentials):
    inventory_page, _ = login_and_get_pages(driver, base_url, credentials)

    inventory_page.logout()

    # After logout, we should be back on login page
    login_button = driver.wait.until(EC.visibility_of_element_located((By.ID, "login-button")))
    assert login_button.is_displayed(), "Login button should be visible after logout"
    assert "inventory.html" not in driver.current_url, "Should no longer be on inventory page"

def test_logout_cart_page(driver, base_url, credentials):
    cart_page, _ = login_and_get_pages(driver, base_url, credentials)

    cart_page.logout()
    login_button = driver.wait.until(EC.visibility_of_element_located((By.ID, "login-button")))
    assert login_button.is_displayed(), "Login button should be visible after logout"
    assert "cart.html" not in driver.current_url, "Should no longer be on cart page"

def test_logout_checkout_page(driver, base_url, credentials):
    checkout_page, _ = login_and_get_pages(driver, base_url, credentials)

    checkout_page.logout()
    login_button = driver.wait.until(EC.visibility_of_element_located((By.ID, "login-button")))
    assert login_button.is_displayed(), "Login button should be visible after logout"
    assert "checkout-step-one.html" not in driver.current_url, "Should no longer be on checkout page"

def test_logout_product_page(driver, base_url, credentials):
    product_page, _ = login_and_get_pages(driver, base_url, credentials)

    product_page.logout()
    login_button = driver.wait.until(EC.visibility_of_element_located((By.ID, "login-button")))
    assert login_button.is_displayed(), "Login button should be visible after logout"
    assert "inventory-item.html" not in driver.current_url, "Should no longer be on product page"