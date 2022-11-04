import time
import pytest
from pages.base import WebPage
from pages.hobbii_pages import Main_Page
from pages.elements import WebElement
from pages.elements import ManyWebElements
from selenium.webdriver import ActionChains


#py -m pytest -v --driver Chrome --driver-path chromedriver.exe test_0.py


def test_add_to_cart(web_browser):
    page = Main_Page(web_browser)
    page.search_input.send_keys("Alpaca")
    page.search_input_btn.click()
    page.wait_page_loaded()
    #page.search_product_cards_one.is_clickable()
    page.search_product_cards_one.click()
    page.wait_page_loaded()
    page.desired_product_card.is_visible()
    #page.desired_product_color.click()
    #page.add_to_cart_btn.click()
    #page.cart_box.click()
    #page.wait_page_loaded()
    #assert page.cart_banner.is_presented()
