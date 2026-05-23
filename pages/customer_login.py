from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import login_locators as loc


class CustomerLogin(BasePage):
    page_url = '/'

    def open_login_window(self):
        self.find(loc.open_login_window_loc).click()


    def fill_login_form(self, login_text, passw_text):
        wait = WebDriverWait(self.driver, 10)
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[name="login"]')))
        passw = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[name="password"]')))
        login.send_keys(login_text)
        passw.send_keys(passw_text)
        self.find(loc.button_sign_in_loc).click()


    def check_error_alert_text_is(self, text):
        wait = WebDriverWait(self.driver, 10)
        error = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'invalid-feedback')))
        assert error.text == text
