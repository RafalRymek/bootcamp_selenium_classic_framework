from selenium.webdriver.common.by import By
from hamcrest import assert_that, has_string
from pages.base_page import BasePage


class ShoppingCartPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    __ORDER_SUMMARY_QUANTITY = (By.XPATH, "//input[@name='quantity_5_19_0_0_hidden']")

    def check_order_summary_quantity(self):
        self.get_element(self.__ORDER_SUMMARY_QUANTITY)
        assert_that(*self.__ORDER_SUMMARY_QUANTITY, has_string("1"))
