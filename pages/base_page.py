class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def go_to_url(self, url):
        self.driver.get(url)

    def get_element(self, by_locator):
        return self.driver.find_element(*by_locator)

    def click(self, by_locator):
        return self.driver.find_element(*by_locator).click()

    def fill(self, by_locator, value):
        return self.driver.find_element(*by_locator).send_keys(value)

    def hover_over_on_element(self, by_locator):
        ActionChains(self.driver).move_to_element(by_locator).perform()
