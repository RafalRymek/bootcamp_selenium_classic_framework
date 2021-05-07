from selenium.webdriver.common.by import By
from hamcrest import assert_that, starts_with
from pages.base_page import BasePage


class ShoppingCartPage(BasePage):

    __ORDER_SUMMARY_QUANTITY = (By.ID, "summary_products_quantity")

    def check_order_summary_quantity(self):
        self.get_element(self.__ORDER_SUMMARY_QUANTITY)
        assert_that(*self.__ORDER_SUMMARY_QUANTITY, starts_with("1"))
