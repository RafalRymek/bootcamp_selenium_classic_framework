from utils.utils import USER_EMAIL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class RegistrationPage(BasePage):

    __FIRST_NAME = (By.XPATH, "//input[@id='customer_firstname']")
    __LAST_NAME = (By.XPATH, "//input[@id='customer_lastname']")
    __PASSWORD = (By.XPATH, "//input[@type='password']")
    __ADDRESS_INPUT = (By.XPATH, "//input[@id='address1']")
    __CITY_INPUT = (By.XPATH, "//input[@id='city']")
    __STATE_PICKER = (By.XPATH, "//select[@id='id_state']/option[text()='Alaska']")
    __ZIP_CODE = (By.XPATH, "//input[@id='postcode']")
    __COUNTRY_PICKER = (By.XPATH, "//select[@id='id_country']/option[text()='United States']")
    __PHONE_NUMBER = (By.XPATH, "//input[@id='phone_mobile']")
    __ALIAS_INPUT = (By.XPATH, "//input[@id='alias']")
    __REGISTER_BUTTON = (By.XPATH, "//button[@id='submitAccount']")

    def user_registration(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.__FIRST_NAME))
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
