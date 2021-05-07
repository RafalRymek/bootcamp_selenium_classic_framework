from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

    __SEARCH_FIELD = (By.ID, "search_query_top")
    __SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    __SIGN_IN_BUTTON = (By.XPATH, "//a[normalize-space()='Sign in']")

    def input_data_into_search_field(self, input_value):
        self.fill(by_locator=self.__SEARCH_FIELD, value=input_value)
        self.click(by_locator=self.__SUBMIT_BUTTON)

    def click_on_sign_in_button(self):
        self.click(by_locator=self.__SIGN_IN_BUTTON)
