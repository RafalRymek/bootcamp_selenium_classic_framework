from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self):
        self.driver = driver

    def get_element(self, by_locator):
        return self.driver.find_element(*by_locator)

    def get_elements(self, by_locator):
        return self.driver.find_elements(*by_locator)

    def click(self, by_locator):
        return self.driver.find_element(*by_locator).click()

    def fill(self, by_locator, value):
        return self.driver.find_element(*by_locator).send_keys(value)

    def hover_over_on_element(self, by_locator):
        ActionChains(self.driver).move_to_element(by_locator).perform()

    def clear(self, by_locator):
        return self.driver.find_element(*by_locator).clear()
