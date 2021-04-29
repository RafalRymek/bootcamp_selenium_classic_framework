from selenium.webdriver.common.by import By
from hamcrest import assert_that, has_string


class ShoppingCartPage:

    def __init__(self, driver):
        self.driver = driver

    order_summary_quantity = (By.XPATH, "//input[@name='quantity_5_19_0_0_hidden']")

    def check_order_summary_quantity(self):
        self.driver.find_element(*self.order_summary_quantity)
        assert_that(*self.order_summary_quantity, has_string("1"))
