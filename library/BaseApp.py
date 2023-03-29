from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://lkp-predprod.lkp-task.boxberry.ru/auth/"

    def wait_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def wait_element_name(self, locator, name, time=10):
        return WebDriverWait(self.driver, time).until(EC.text_to_be_present_in_element(locator, name),
                                                      message=f"Can't find elements by locator {locator}, Can't find text '{name}'")

    def click_the_element(self, button_element):
        return button_element.click()

    def send_keys(self, key_element, key):
        return key_element.send_keys(key)

    def go_to_site(self):
        return self.driver.get(self.base_url)