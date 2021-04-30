import unittest

from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from utils.utils import SEARCH_INPUT, DRESS_INPUT, BASE_URL, USER_EMAIL
from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.authentication_page import AuthenticationPage
from pages.registration_page import RegistrationPage
from pages.shopping_cart_page import ShoppingCartPage


class MySeleniumTests(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
        self.driver.implicitly_wait(3)
        self.driver.set_window_size(1440, 900)
        self.driver.get(BASE_URL)

        self.main_page = MainPage(driver=self.driver)
        self.search_page = SearchPage(driver=self.driver)
        self.authentication_page = AuthenticationPage(driver=self.driver)
        self.registration_page = RegistrationPage(driver=self.driver)
        self.shopping_cart_page = ShoppingCartPage(driver=self.driver)

        self.driver.get(BASE_URL)

    def test_search(self):
        self.main_page.input_data_into_search_field(SEARCH_INPUT)
        self.search_page.check_amount_of_search_results()

    def test_registration(self):
        self.main_page.click_on_sign_in_button()
        self.authentication_page.input_email_for_registration(user_email=USER_EMAIL)
        self.registration_page.user_registration()

    def test_add_to_cart(self):
        self.main_page.input_data_into_search_field(DRESS_INPUT)
        self.search_page.hover_over_on_first_result()
        self.search_page.add_product_to_basket()
        self.search_page.move_to_shopping_cart()
        self.search_page.click_button_order_cart()
        self.shopping_cart_page.check_order_summary_quantity()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

