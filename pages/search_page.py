from selenium.webdriver.common.by import By
from hamcrest import assert_that, has_string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class SearchPage:

    def __init__(self, driver):
        self.driver = driver

    product_container = (By.XPATH, "//div[@class='product-container']")
    amount_text = (By.CSS_SELECTOR, ".heading-counter")
    add_to_cart = (By.XPATH, "//a[@class='button ajax_add_to_cart_button btn btn-default']")
    success_added_icon = (By.XPATH, "//i[@class='icon-ok']")
    success_header = (By.XPATH, "//h2")
    close_pop_up = (By.XPATH, "//span[@title='Close window']")
    shopping_cart = (By.XPATH, "//a[@title='View my shopping cart']")
    button_order_cart = (By.XPATH, "//a[@id='button_order_cart']")

    def check_amount_of_search_results(self):
        search_result = self.driver.find_element(*self.amount_text)
        assert_that(search_result.text, has_string("5 results have been found."), reason="Wrong amount of products")

    def hover_over_on_first_result(self):
        first_item = self.driver.find_elements(*self.product_container)[0]
        sleep(2)
        ActionChains(self.driver).move_to_element(first_item).perform()

    def add_product_to_basket(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_to_cart)).click()
        self.driver.find_element(*self.close_pop_up).click()

    def move_to_shopping_cart(self):
        cart_icon = self.driver.find_element(*self.shopping_cart)
        ActionChains(self.driver).move_to_element(cart_icon).perform()

    def click_button_order_cart(self):
        self.driver.find_element(*self.button_order_cart).click()

