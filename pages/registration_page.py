from utils.utils import USER_EMAIL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver

    first_name = (By.XPATH, "//input[@id='customer_firstname']")
    last_name = (By.XPATH, "//input[@id='customer_lastname']")
    password = (By.XPATH, "//input[@type='password']")
    address_first_name = (By.XPATH, "//input[@id='firstname']")
    address_last_name = (By.XPATH, "//input[@id='lastname']")
    address_input = (By.XPATH, "//input[@id='address1']")
    city_input = (By.XPATH, "//input[@id='city']")
    state_picker = (By.XPATH, "//select[@id='id_state']/option[text()='Alaska']")
    zip_code = (By.XPATH, "//input[@id='postcode']")
    country_picker = (By.XPATH, "//select[@id='id_country']/option[text()='United States']")
    phone_number = (By.XPATH, "//input[@id='phone_mobile']")
    alias_input = (By.XPATH, "//input[@id='alias']")
    register_button = (By.XPATH, "//button[@id='submitAccount']")

    def user_registration(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.first_name))
        self.driver.find_element(*self.first_name).send_keys("Tester")
        self.driver.find_element(*self.last_name).send_keys("Testers")
        self.driver.find_element(*self.password).send_keys("123456")
        self.driver.find_element(*self.address_input).send_keys("Brain street")
        self.driver.find_element(*self.city_input).send_keys("Cracow")
        self.driver.find_element(*self.state_picker).click()
        self.driver.find_element(*self.zip_code).send_keys("00000")
        self.driver.find_element(*self.country_picker)
        self.driver.find_element(*self.phone_number).send_keys("111222333")
        self.driver.find_element(*self.alias_input).clear()
        self.driver.find_element(*self.alias_input).send_keys("test@test.com")
        self.driver.find_element(*self.register_button).click()
