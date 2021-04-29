from utils.utils import USER_EMAIL
from selenium.webdriver.common.by import By
from hamcrest import assert_that, starts_with


class AuthenticationPage:

    def __init__(self, driver):
        self.driver = driver

    email_field = (By.XPATH, "//input[@class='is_required validate account_input form-control']")
    create_submit_button = (By.XPATH, "//button[@class='btn btn-default button button-medium exclusive']")
    account_information = (By.XPATH, "//p[@class='info-account']")

    def input_email_for_registration(self, user_email):
        self.driver.find_element(*self.email_field).send_keys(user_email)
        self.driver.find_element(*self.create_submit_button).click()

    def confirmation_user_successful_registration(self):
        self.driver.find_element(*self.account_information)
        assert_that(*self.account_information, starts_with("Welcome"))
