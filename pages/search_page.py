from selenium.webdriver.common.by import By
from hamcrest import assert_that, has_string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base_page import BasePage


class SearchPage(BasePage):

    __PRODUCT_CONTAINER = (By.XPATH, "//div[@class='product-container']")
    __AMOUNT_TEXT = (By.CSS_SELECTOR, ".heading-counter")
    __ADD_TO_CART_BUTTON = (By.XPATH, "//span[contains(text(), 'Add to cart')]")
    __CLOSE_POP_UP = (By.XPATH, "//span[@title='Close window']")
    __SHOPPING_CART = (By.XPATH, "//a[@title='View my shopping cart']")
    __BUTTON_ORDER_CART = (By.ID, "button_order_cart")

    def check_amount_of_search_results(self):
        search_result = self.get_element(self.__AMOUNT_TEXT)
        assert_that(search_result.text, has_string("5 results have been found."), reason="Wrong amount of products")

    def hover_over_on_first_result(self):
        first_item = self.get_elements(self.__PRODUCT_CONTAINER)[0]
        sleep(2)
        self.hover_over_on_element(by_locator=first_item)

    def add_product_to_basket(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__ADD_TO_CART_BUTTON))
        self.click(by_locator=self.__ADD_TO_CART_BUTTON)
        self.click(by_locator=self.__CLOSE_POP_UP)

    def move_to_shopping_cart(self):
        cart_icon = self.get_element(self.__SHOPPING_CART)
        self.hover_over_on_element(by_locator=cart_icon)

    def click_button_order_cart(self):
        self.click(by_locator=self.__BUTTON_ORDER_CART)

