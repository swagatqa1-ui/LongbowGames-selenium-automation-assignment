from selenium.webdriver.common.by import By

class InventoryPage:

    def __init__(self, driver):
        self.driver = driver

    def is_loaded(self):
        return "inventory" in self.driver.current_url

    def open_first_product(self):
        self.driver.find_element(By.CLASS_NAME, "inventory_item_name").click()

    def get_product_title(self):
        return self.driver.find_element(By.CLASS_NAME, "inventory_details_name").text
