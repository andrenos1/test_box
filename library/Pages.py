from library.BaseApp import BasePage
from selenium.webdriver.common.by import By


class PagesHelper(BasePage):

    def wait_object_by_CLASS(self, locator):
        elements = self.wait_element((By.CLASS_NAME, locator), time=2)
        return elements

    def wait_object_by_XPATH(self, locator):
        elements = self.wait_element((By.XPATH, locator), time=2)
        return elements

    def wait_object_and_name_by_XPATH(self, locator, name):
        elements = self.wait_element_name((By.XPATH, locator), name, time=2)
        return elements
