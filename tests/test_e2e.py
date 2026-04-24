from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_user_journey(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    # Open site
    login.open()

    # Login
    login.login("standard_user", "secret_sauce")

    # Validation 1: Inventory page loaded
    assert inventory.is_loaded()

    # Open product
    inventory.open_first_product()

    # Validation 2: Product title exists
    assert inventory.get_product_title() != ""
