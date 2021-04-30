from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    __SEARCH_FIELD = (By.XPATH, "//input[@class='search_query form-control ac_input']")
    __SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    __SIGN_IN_BUTTON = (By.XPATH, "//a[@class='login']")

    def input_data_into_search_field(self, input_value):
        self.fill(by_locator=self.__SEARCH_FIELD, value=input_value)
        self.click(by_locator=self.__SUBMIT_BUTTON)

    def click_on_sign_in_button(self):
        self.click(by_locator=self.__SIGN_IN_BUTTON)
