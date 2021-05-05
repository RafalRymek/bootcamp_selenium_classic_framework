import unittest

import time
from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.authentication_page import AuthenticationPage
from pages.registration_page import RegistrationPage
from pages.shopping_cart_page import ShoppingCartPage


class MySeleniumTests(unittest.TestCase):

    BASE_URL = "http://automationpractice.com/index.php"
    USER_EMAIL = "test" + str(time.time() * 1000) + "@test.com"

    def setUp(self):

        self.main_page = MainPage()
        self.search_page = SearchPage()
        self.authentication_page = AuthenticationPage()
        self.registration_page = RegistrationPage()
        self.shopping_cart_page = ShoppingCartPage()

        self.search_page.go_to_url(url=self.BASE_URL)

    def test_search(self):
        self.main_page.input_data_into_search_field(input_value="Printed dress")
        self.search_page.check_amount_of_search_results()

    def test_registration(self):
        self.main_page.click_on_sign_in_button()
        self.authentication_page.input_email_for_registration(user_email=self.USER_EMAIL)
        self.registration_page.user_registration()
        self.authentication_page.confirmation_user_successful_registration()

    def test_add_to_cart(self):
        self.main_page.input_data_into_search_field(input_value="Dress")
        self.search_page.hover_over_on_first_result()
        self.search_page.add_product_to_basket()
        self.search_page.move_to_shopping_cart()
        self.search_page.click_button_order_cart()
        self.shopping_cart_page.check_order_summary_quantity()

    def tearDown(self):
        self.search_page.quite_driver()


if __name__ == '__main__':
    unittest.main()

