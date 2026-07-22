import pytest

@pytest.mark.smoke
def test_empty_password(login_page):
    login_page.open_page()
    login_page.open_login_window()
    login_page.fill_login_form('sassss@basss.sss', '')
    login_page.check_error_alert_text_is('Необходимо заполнить поле «Пароль».')


@pytest.mark.regression
def test_incorrect_password(login_page):
    login_page.open_page()
    login_page.open_login_window()
    login_page.fill_login_form('dmitro.p.vladimirovich@gmail.com', 'dddd')
    login_page.check_error_alert_text_is('Неправильный пароль.')