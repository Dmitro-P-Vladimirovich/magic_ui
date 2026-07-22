import pytest


@pytest.mark.extended
def test_header_title(shops_page):
    shops_page.open_page()
    shops_page.check_page_header_title_is('Наши магазины')