import time
import pytest
from pages.base import WebPage
from pages.hobbii_pages import Main_Page
from pages.elements import WebElement
from selenium.webdriver import ActionChains

# py -m pytest -v --driver Chrome --driver-path chromedriver.exe test_hobbii_login.py


# 1-4 Проверка окошка ввода логина

def test_login_input_clickable(web_browser):
    page = Main_Page(web_browser)
    page.wait_page_loaded()

    assert page.login_input.is_visible()
    assert page.login_input.is_clickable()


def test_login_container_present(web_browser):
    page = Main_Page(web_browser)
    page.login_input.wait_to_be_clickable()
    page.login_input.click()
    page.wait_page_loaded()

    assert page.login_container.is_presented()


def test_login_contains_elements_visible(web_browser):
    page = Main_Page(web_browser)
    page.login_input.wait_to_be_clickable()
    page.login_input.click()
    page.wait_page_loaded()

    assert page.input_email.is_visible()
    assert page.input_password.is_visible()
    assert page.in_account_btn.is_visible()


def test_login_register_container_present(web_browser):
    page = Main_Page(web_browser)
    page.login_input.wait_to_be_clickable()
    page.login_input.click()
    page.wait_page_loaded()
    page.login_register.click()

    assert page.get_current_url() == 'https://hobbii.com/account/signup'
    assert page.login_register_container.is_presented()


# 4 Проверка правильного ввода логина

def test_positive_account_input(web_browser):
    page = Main_Page(web_browser)
    page.login_input.wait_to_be_clickable()
    page.login_input.click()
    page.wait_page_loaded()
    page.input_email = 'ok.brede@inbox.lv'
    page.input_password = 'brede73'
    page.in_account_btn.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://hobbii.com/account/account'


# 5-8 Проверка неправильного ввода логина

def test_negative_account_email_input(web_browser):
    page = Main_Page(web_browser)
    page.login_input.wait_to_be_clickable()
    page.login_input.click()
    page.wait_page_loaded()
    page.input_email = 'ok.brede@in.lv'
    page.input_password = 'brede73'
    page.in_account_btn.click()
    page.wait_page_loaded()

    assert page.login_error.is_presented()


def test_negative_account_password_input(web_browser):
    page = Main_Page(web_browser)
    page.login_input.wait_to_be_clickable()
    page.login_input.click()
    page.wait_page_loaded()
    page.input_email = 'ok.brede@inbox.lv'
    page.input_password = 'bebebeb'
    page.in_account_btn.click()
    page.wait_page_loaded()

    assert page.login_error.is_presented()


def test_negative_account_email_forgot(web_browser):
    page = Main_Page(web_browser)
    page.login_input.wait_to_be_clickable()
    page.login_input.click()
    page.wait_page_loaded()
    page.input_email = 'ok.bre@inbox.lv'
    page.input_password = 'brede73'
    page.in_account_btn.click()
    page.wait_page_loaded()
    page.forgotten_password_btn.click()

    assert page.get_current_url() == 'https://hobbii.com/account/forgotten?identifier=ok.bre%40inbox.lv'
    assert page.forgotten_container.is_presented()


def test_negative_account_password_forgot(web_browser):
    page = Main_Page(web_browser)
    page.login_input.wait_to_be_clickable()
    page.login_input.click()
    page.wait_page_loaded()
    page.input_email = 'ok.brede@inbox.lv'
    page.input_password = 'bebebeb'
    page.in_account_btn.click()
    page.wait_page_loaded()
    page.forgotten_password_btn.click()

    assert page.get_current_url() == 'https://hobbii.com/account/forgotten?identifier=ok.bre%40inbox.lv'
    assert page.forgotten_container.is_presented()


# 9

