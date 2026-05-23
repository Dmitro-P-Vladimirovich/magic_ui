from pages.base_page import BasePage
from pages.locators import shops_page_locators as loc

class ShopsPage(BasePage):
    page_url = '/shops'
    def check_page_header_title_is(self, text):
        header_title = self.find(loc.header_title_loc)
        assert header_title.text == text