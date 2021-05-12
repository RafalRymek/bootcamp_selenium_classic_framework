from selenium.webdriver.common.by import By
from hamcrest import assert_that, has_string
from time import sleep
from pages.base_page import BasePage


class SearchPage(BasePage):

    # __PRODUCT_CONTAINER = (By.XPATH, "//div[@class='product-container']")
    __FIRST_DRESS = (By.XPATH, "//ul[contains(@class,'product_list')]/li[1]")
    __AMOUNT_TEXT = (By.CSS_SELECTOR, ".heading-counter")
    __ADD_TO_CART_BUTTON = (By.XPATH, "//span[text()='Add to cart']")
    __CLOSE_POP_UP = (By.XPATH, "//span[@title='Close window']")
    __SHOPPING_CART = (By.XPATH, "//a[@title='View my shopping cart']")
    __BUTTON_ORDER_CART = (By.ID, "button_order_cart")

    def check_amount_of_search_results(self):
        search_result = self.get_element(self.__AMOUNT_TEXT)
        assert_that(search_result.text, has_string("5 results have been found."), reason="Wrong amount of products")

    def hover_over_on_first_result(self):
        self.hover_over_on_element(by_locator=self.__FIRST_DRESS)

    def add_product_to_basket(self):
        self.click(by_locator=self.__ADD_TO_CART_BUTTON)
        self.click(by_locator=self.__CLOSE_POP_UP)

    def move_to_shopping_cart(self):
        self.hover_over_on_element(by_locator=self.__SHOPPING_CART)

    def click_button_order_cart(self):
        self.click(by_locator=self.__BUTTON_ORDER_CART)

