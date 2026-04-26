import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

@pytest.fixture
def login_page(page):
    lp = LoginPage(page)
    lp.abrir()
    return lp

def test_login_valido(login_page, page):
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in page.url

def test_login_usuario_bloqueado(login_page):
    login_page.login("locked_out_user", "secret_sauce")
    assert "Epic sadface" in login_page.obtener_error()

def test_login_invalido(login_page):
    login_page.login("usuario_malo", "pass_mala")
    assert "Epic sadface" in login_page.obtener_error()

def test_login_sin_usuario(login_page):
    login_page.login("", "secret_sauce")
    assert "Username is required" in login_page.obtener_error()

def test_login_sin_password(login_page):
    login_page.login("standard_user", "")
    assert "Password is required" in login_page.obtener_error()
