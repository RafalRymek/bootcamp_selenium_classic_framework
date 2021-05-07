from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegistrationPage(BasePage):

    __FIRST_NAME = (By.ID, "customer_firstname")
    __LAST_NAME = (By.ID, "customer_lastname")
    __PASSWORD = (By.XPATH, "//input[@type='password']")
    __ADDRESS_INPUT = (By.ID, "address1")
    __CITY_INPUT = (By.ID, "city")
    __STATE_PICKER = (By.XPATH, "//select[@id='id_state']/option[text()='Alaska']")
    __ZIP_CODE = (By.ID, "postcode")
    __COUNTRY_PICKER = (By.XPATH, "//select[@id='id_country']/option[text()='United States']")
    __PHONE_NUMBER = (By.ID, "phone_mobile")
    __ALIAS_INPUT = (By.ID, "alias")
    __REGISTER_BUTTON = (By.ID, "submitAccount")

    def user_registration(self):
        self.is_element_visible(self.__FIRST_NAME)
        self.fill(by_locator=self.__FIRST_NAME, value="Tester")
        self.fill(by_locator=self.__LAST_NAME, value="Testers")
        self.fill(by_locator=self.__PASSWORD, value="123456")
        self.fill(by_locator=self.__ADDRESS_INPUT, value="Brain avenue")
        self.fill(by_locator=self.__CITY_INPUT, value="Cracow")
        self.click(by_locator=self.__STATE_PICKER)
        self.fill(by_locator=self.__ZIP_CODE, value="00000")
        self.fill(by_locator=self.__PHONE_NUMBER, value="111222333")
        self.clear(by_locator=self.__ALIAS_INPUT)
        self.fill(by_locator=self.__ALIAS_INPUT, value="test@test.com")
        self.click(by_locator=self.__REGISTER_BUTTON)
