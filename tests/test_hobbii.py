import time
import pytest
from pages.base import WebPage
from pages.hobbii_pages import Main_Page
from pages.elements import WebElement
from selenium.webdriver import ActionChains

# py -m pytest -v --driver Chrome --driver-path chromedriver.exe test_hobbii.py


# 1 Наличие основных элементов на главной странице

def test_start_page_main_elements(web_browser):
    page = Main_Page(web_browser)
    assert page.top_sale.is_visible()
    assert page.general_logo.is_visible()
    assert page.general_menu.is_visible()
    assert page.top_sale.is_clickable()
    assert page.general_logo.is_clickable()
    assert page.footer.is_visible()


# 02-11 Проверка кнопок верхнего(малого) меню

def test_menu_blog_url(web_browser):
    page = Main_Page(web_browser)
    page.blog_btn.click()
    assert page.get_current_url() == 'https://hobbii.com/blog'


def test_menu_blog(web_browser):
    page = Main_Page(web_browser)
    page.blog_btn.click()
    assert page.blog_categories.is_visible()


def test_menu_hobbii_plus_url(web_browser):
    page = Main_Page(web_browser)
    page.hobbii_plus_btn.click()
    assert page.get_current_url() == 'https://hobbii.com/plus'


def test_menu_hobbii_plus(web_browser):
    page = Main_Page(web_browser)
    page.hobbii_plus_btn.click()
    assert page.hobbii_benefit.is_visible()


def test_menu_point_url(web_browser):
    page = Main_Page(web_browser)
    page.point_btn.click()
    assert page.get_current_url() == 'https://hobbii.com/pointshop'


def test_menu_point(web_browser):
    page = Main_Page(web_browser)
    page.point_btn.click()
    assert page.poin_store.is_visible()


def test_menu_help_contact_url(web_browser):
    page = Main_Page(web_browser)
    page.help_contact_btn.click()
    assert page.get_current_url() == 'https://hobbii.com/hobbii-faq'


def test_menu_help_contact(web_browser):
    page = Main_Page(web_browser)
    page.help_contact_btn.click()
    assert page.help_contact_menu.is_visible()


def test_menu_about_url(web_browser):
    page = Main_Page(web_browser)
    page.about_btn.click()
    assert page.get_current_url() == 'https://hobbii.com/about'


def test_menu_about(web_browser):
    page = Main_Page(web_browser)
    page.about_btn.click()
    assert page.about_hobbii.is_visible()


# 12-13 Проверка главного лого

def test_general_logo_1(web_browser):
    page = Main_Page(web_browser)
    page.blog_btn.click()

    page.general_logo.click()
    assert page.get_current_url() == 'https://hobbii.com/'


def test_general_logo_2(web_browser):
    page = Main_Page(web_browser)
    page.about_btn.click()

    page.general_logo.click()
    assert page.get_current_url() == 'https://hobbii.com/'


# 14-23 Проверка кнопок главного меню

def test_general_menu_elements_visible(web_browser):
    page = Main_Page(web_browser)
    assert page.gen_menu_home.is_visible()
    assert page.gen_menu_yarn.is_visible()
    assert page.gen_menu_patterns.is_visible()
    assert page.gen_menu_crochetHooks.is_visible()
    assert page.gen_menu_knittingNeedles.is_visible()
    assert page.gen_menu_accessories.is_visible()
    assert page.gen_menu_excitingThings.is_visible()


def test_general_menu_elements_clickable(web_browser):
    page = Main_Page(web_browser)
    assert page.gen_menu_home.is_clickable()
    assert page.gen_menu_yarn.is_clickable()
    assert page.gen_menu_patterns.is_clickable()
    assert page.gen_menu_crochetHooks.is_clickable()
    assert page.gen_menu_knittingNeedles.is_clickable()
    assert page.gen_menu_accessories.is_clickable()
    assert page.gen_menu_excitingThings.is_clickable()


def test_gen_menu_yarn_url(web_browser):
    page = Main_Page(web_browser)
    page.gen_menu_yarn.click()
    assert page.get_current_url() == 'https://hobbii.com/yarn'


def test_gen_yarn_home(web_browser):
    page = Main_Page(web_browser)
    page.gen_menu_yarn.click()
    assert page.yarn_fibers.is_visible()


def test_gen_menu_patterns_url(web_browser):
    page = Main_Page(web_browser)
    page.gen_menu_patterns.click()
    assert page.get_current_url() == 'https://hobbii.com/product-patterns'


def test_gen_menu_patterns_home(web_browser):
    page = Main_Page(web_browser)
    page.gen_menu_patterns.click()
    assert page.yarn_fibers.is_visible()


def test_gen_menu_crochetHooks_url(web_browser):
    page = Main_Page(web_browser)
    page.gen_menu_crochetHooks.click()
    assert page.get_current_url() == 'https://hobbii.com/crochet-hooks'


def test_gen_menu_crochetHooks_home(web_browser):
    page = Main_Page(web_browser)
    page.gen_menu_crochetHooks.click()
    assert page.crochetHooks_category.is_visible()


def test_gen_menu_knittingNeedles_url(web_browser):
    page = Main_Page(web_browser)
    page.gen_menu_knittingNeedles.click()
    assert page.get_current_url() == 'https://hobbii.com/knitting-needles'


def test_gen_menu_knittingNeedles_home(web_browser):
    page = Main_Page(web_browser)
    page.gen_menu_knittingNeedles.click()
    assert page.knittingNeedles_page.is_visible()


# 24-25 Предподвал

def test_about_hobbii_history(web_browser):
    page = Main_Page(web_browser)

    page.wait_page_loaded()
    assert page.about_hobbii_box.is_presented()


def test_reviews_list_present(web_browser):
    page = Main_Page(web_browser)
    page.reviews_box.scroll_to_element()
    page.wait_page_loaded()

    assert page.reviews_list.is_visible()
    assert page.reviews_trustpilot.is_clickable()



# 26-29 Иконки соцсетей

def test_instagram_link(web_browser):
    page = Main_Page(web_browser)
    page.scroll_down()
    page.instagram_btn.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    page.wait_page_loaded()
    if page.instagram_cookie.is_presented():
        page.instagram_yes.click()
        page.wait_page_loaded()
        assert page.get_current_url() == 'https://www.instagram.com/hobbii_yarn/'


def test_facebook_link(web_browser):
    page = Main_Page(web_browser)
    page.scroll_down()
    page.facebook_btn.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    page.wait_page_loaded()
    if page.facebook_cookie.is_presented():
        page.facebook_yes.click()
        page.wait_page_loaded()
        assert page.get_current_url() == 'https://www.facebook.com/hobbii.europe/'


def test_pinterest_link(web_browser):
    page = Main_Page(web_browser)
    page.scroll_down()
    page.pinterest_btn.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://www.pinterest.com/hobbiicom/'


def test_youtube_btn(web_browser):
    page = Main_Page(web_browser)
    page.scroll_down()
    page.youtube_btn.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    page.wait_page_loaded()
    if page.youtube_list.is_presented():
        page.youtube_yes.click()
        assert page.get_current_url() == 'https://www.youtube.com/c/hobbiicom'


# 30 Ссылки в подвале сайта

def test_footer_list(web_browser):
    page = Main_Page(web_browser)
    page.scroll_down()
    assert page.contact.is_presented()
    assert page.about_as.is_presented()
    assert page.fun_stuff.is_presented()
    assert page.follow_as.is_presented()


def test_reviews_list_trustpilot(web_browser):
    page = Main_Page(web_browser)
    page.reviews_box.scroll_to_element()
    page.reviews_trustpilot.wait_to_be_clickable()
    page.reviews_trustpilot.click()

    web_browser.switch_to.window(web_browser.window_handles[1])
    page.wait_page_loaded()

    if page.police_title.is_visible():
        page.cookies_ok.click()
        assert page.get_current_url() == 'https://uk.trustpilot.com/review/hobbii.co.uk?utm_medium=trustbox&utm_source=Carousel'


