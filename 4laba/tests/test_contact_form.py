import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.contact_page import ContactPage

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_valid_contact_form(driver):
    page = ContactPage(driver)
    page.open("file:///D:/тестированиеПО/Software-testing/4laba/contact.html")  # путь к файлу

    page.fill_form("Илья", "test@example.com", "Привет, мир")
    page.submit()

    assert "Форма успешно отправлена!" in page.get_result_message()

def test_invalid_contact_form(driver):
    page = ContactPage(driver)
    page.open("file:///D:/тестированиеПО/Software-testing/4laba/contact.html")

    # оставляем имя пустым
    page.fill_form("", "test@example.com", "Привет, мир")
    page.submit()

    assert "Исправьте ошибки!" in page.get_result_message()
