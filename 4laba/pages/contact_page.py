from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ContactPage(BasePage):
    NAME = (By.ID, "name")
    EMAIL = (By.ID, "email")
    MESSAGE = (By.ID, "message")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    RESULT = (By.ID, "formResult")

    def fill_form(self, name, email, message):
        self.type(*self.NAME, text=name)
        self.type(*self.EMAIL, text=email)
        self.type(*self.MESSAGE, text=message)

    def submit(self):
        self.click(*self.SUBMIT)

    def get_result_message(self):
        return self.get_text(*self.RESULT)
