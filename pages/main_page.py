from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    search_field = (By.XPATH, "//input[@class='search_query form-control ac_input']")
    submit_button = (By.XPATH, "//button[@type='submit']")
    sign_in_button = (By.XPATH, "//a[@class='login']")

    def input_data_into_search_field(self, by_locator):
        self.driver.find_element(*self.search_field).send_keys(by_locator)
        self.driver.find_element(*self.submit_button).click()

    def click_on_sign_in_button(self):
        self.driver.find_element(*self.sign_in_button).click()
