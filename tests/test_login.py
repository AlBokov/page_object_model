from pages.pages import LoginPage
import requests

def test_login_fail(browser):
    page = LoginPage(browser)
    page.open()
    page.login("standard_user", "wrong_pass")
    assert "Username and password do not match" in page.get_error_message()


def test_login_pass(browser):
    page = LoginPage(browser)
    page.open()
    page.login("standard_user", "secret_sauce")
    assert "Products" in page.get_pass_login()

def test_login_block(browser):
    page = LoginPage(browser)
    page.open()
    page.login("locked_out_user", "secret_sauce")
    assert "Sorry, this user has been locked out." in page.get_error_message()