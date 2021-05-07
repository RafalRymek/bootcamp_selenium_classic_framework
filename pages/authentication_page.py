from selenium.webdriver.common.by import By
from hamcrest import assert_that, starts_with
from pages.base_page import BasePage


class AuthenticationPage(BasePage):

    __EMAIL_FIELD = (By.ID, "email_create")
    __CREATE_SUBMIT_BUTTON = (By.ID, "SubmitCreate")
    __ACCOUNT_INFORMATION = (By.XPATH, "//h1[text()='My account']")

    def input_email_for_registration(self, user_email):
        self.is_element_visible(by_locator=self.__EMAIL_FIELD)
        self.fill(by_locator=self.__EMAIL_FIELD, value=user_email)
        self.click(by_locator=self.__CREATE_SUBMIT_BUTTON)

    def confirmation_user_successful_registration(self):
        self.is_element_visible(by_locator=self.__ACCOUNT_INFORMATION)
        assert_that(*self.__ACCOUNT_INFORMATION, starts_with("Welcome"))
