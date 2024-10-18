from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # Время ожидания

    def open_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except (TimeoutException, NoSuchElementException) as e:
            raise Exception(f"Element not found: {locator}") from e

    def click_to_element(self, locator):
        element = self.find_element(locator)
        element.click()

    def get_text(self, locator):
        try:
            element = self.find_element(locator)
            return element.text
        except NoSuchElementException as e:
            raise Exception(f"Element not found: {locator}") from e

    def set_text(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    def scroll(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_cookies(self, locator):
        try:
            element = self.find_element(locator)
            element.click()
        except NoSuchElementException as e:
            raise Exception(f"Element not found: {locator}") from e

    def wait_navigating_url(self, url):
        try:
            self.wait.until(EC.url_changes(url))
        except TimeoutException:
            raise Exception(f"URL did not change to {url}")

    def tab_switch(self):
        self.driver.switch_to.window(self.driver.window_handles[1])