from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click_element(self, *locator):
        self.find_element(*locator).click()

    def send_text(self, text, *locator):
        self.find_element(*locator).send_keys(text)

    def clear_text(self, *locator):
        self.find_element(*locator).clear()

        return self

    def wait_element(self, method, message=''):
        return self.wait.until(ec.element_to_be_clickable(method), message)

    def find_elements(self, index, *element):
        self.driver.find_elements(*element)[index].click()