from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_invalid_login(driver):
    driver.find_element(By.ID, "user-name").send_keys("wrong_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    error = driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
    assert "Username and password do not match" in error.text

def test_login_success(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
    assert "inventory.html" in driver.current_url


def test_add_items_to_cart(driver):
    test_login_success(driver)

    add_buttons = driver.find_elements(By.XPATH, "//button[text()='Add to cart']")
    for button in add_buttons[:3]:
        button.click()

    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "3"


def test_go_to_cart(driver):
    test_add_items_to_cart(driver)

    driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
    assert "cart.html" in driver.current_url


def test_remove_item_cart(driver):
    test_add_items_to_cart(driver)

    driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()

    remove_button = driver.wait.until(EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack")))
    remove_button.click()

    driver.wait.until(lambda d: d.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "2")

    items_in_cart = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(items_in_cart) == 2


def test_checkout_step_one(driver):
    test_add_items_to_cart(driver)

    driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Aleksei")
    driver.find_element(By.ID, "last-name").send_keys("Ivanov")
    driver.find_element(By.ID, "postal-code").send_keys("95621")
    driver.find_element(By.ID, "continue").click()

    driver.wait.until(EC.url_contains("checkout-step-two.html"))
    driver.wait.until(EC.presence_of_element_located((By.ID, "finish")))


def test_checkout_complete(driver):
    test_checkout_step_one(driver)
    driver.find_element(By.ID, "finish").click()

    thank_you = driver.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "complete-header")))
    assert "Thank you for your order!" in thank_you.text