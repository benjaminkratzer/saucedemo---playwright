import pytest
from pages.login_page import LoginPage

@pytest.fixture
def logged_in(page):
    login = LoginPage(page)
    login.abrir()
    login.login("standard_user", "secret_sauce")
    return page
