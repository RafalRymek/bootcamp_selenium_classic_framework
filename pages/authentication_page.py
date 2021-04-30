from selenium.webdriver.common.by import By
from hamcrest import assert_that, starts_with
from pages.base_page import BasePage


class AuthenticationPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    __EMAIL_FIELD = (By.XPATH, "//input[@class='is_required validate account_input form-control']")
    __CREATE_SUBMIT_BUTTON = (By.XPATH, "//button[@class='btn btn-default button button-medium exclusive']")
    __ACCOUNT_INFORMATION = (By.XPATH, "//p[@class='info-account']")

    def input_email_for_registration(self, user_email):
        self.fill(by_locator=self.__EMAIL_FIELD, value=user_email)
        self.click(by_locator=self.__CREATE_SUBMIT_BUTTON)

    def confirmation_user_successful_registration(self):
        self.get_element(by_locator=self.__ACCOUNT_INFORMATION)
        assert_that(*self.__ACCOUNT_INFORMATION, starts_with("Welcome"))
