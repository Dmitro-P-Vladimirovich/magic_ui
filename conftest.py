from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from pages.customer_login import CustomerLogin
from pages.shops_page import ShopsPage


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def login_page(driver):
    return CustomerLogin(driver)

@pytest.fixture()
def shops_page(driver):
    return ShopsPage(driver)


