def test_incorrect_login(login_page):
    login_page.open_page()
    login_page.open_login_window()
    login_page.fill_login_form('sassss@basss.sss', '')
    login_page.check_error_alert_text_is('Необходимо заполнить поле «Пароль».')
