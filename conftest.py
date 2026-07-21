from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from pages.customer_login import CustomerLogin
from pages.shops_page import ShopsPage
import random
import allure


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')  # Обязательно для запуска от root/SYSTEM
    options.add_argument('--disable-dev-shm-usage')  # Обязательно для Docker (обходит нехватку памяти /dev/shm)
    options.add_argument('--disable-gpu')  # Дополнительная стабильность для headless
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(5)
    yield chrome_driver
    # filename = f'{str(random.randint(100, 10000))}.png'
    # chrome_driver.save_screenshot(filename)
    allure.attach(chrome_driver.get_screenshot_as_png(), name="Screenshot", attachment_type="AttachmentType.png")
    chrome_driver.quit()


@pytest.fixture()
def login_page(driver):
    return CustomerLogin(driver)

@pytest.fixture()
def shops_page(driver):
    return ShopsPage(driver)


