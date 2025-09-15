from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Настройки эмулятора и приложения
options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "16"
options.device_name = "emulator-5554"
options.automation_name = "UiAutomator2"
options.app = r"C:\Users\user\AndroidStudioProjects\7labatesting\app\build\outputs\apk\debug\app-debug.apk"
options.app_package = "com.example.a7labatesting"
options.app_activity = ".MainActivity"


driver = None

try:
    # Инициализация драйвера
    driver = webdriver.Remote('http://localhost:4723', options=options)
    print("Приложение запущено успешно!")

    # Ждем загрузки
    time.sleep(2)
    # Ждем 3 секунды чтобы увидеть результат
    time.sleep(3)

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрываем приложение, если driver был создан
    if driver is not None:
        driver.quit()
    print("Тест завершен")
