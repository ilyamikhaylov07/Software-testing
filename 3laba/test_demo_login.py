import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_valid_login(driver):
    username = "tomsmith"
    password = "SuperSecretPassword!"
    driver.get("https://the-internet.herokuapp.com/login")

    # ввод логина
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys(username)

    # ввод пароля
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(password)

    # клик по кнопке
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    # проверка — появилось сообщение об успешном входе
    success_message = driver.find_element(By.ID, "flash")
    assert "You logged into a secure area!" in success_message.text
