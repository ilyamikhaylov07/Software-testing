from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self, url):
        self.driver.get(url)

    def find(self, by, locator):
        return self.wait.until(ec.presence_of_element_located((by, locator)))

    def click(self, by, locator):
        self.find(by, locator).click()

    def type(self, by, locator, text):
        self.find(by, locator).clear()
        self.find(by, locator).send_keys(text)

    def get_text(self, by, locator):
        return self.find(by, locator).text
