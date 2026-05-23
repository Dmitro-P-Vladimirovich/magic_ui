from selenium import webdriver
import pytest
from pages.customer_login import CustomerLogin
from pages.shops_page import ShopsPage


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def login_page(driver):
    return CustomerLogin(driver)

@pytest.fixture()
def shops_page(driver):
    return ShopsPage(driver)


