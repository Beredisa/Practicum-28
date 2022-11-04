import time
import pytest
from pages.base import WebPage
from pages.hobbii_pages import Main_Page
from pages.elements import WebElement
from selenium.webdriver import ActionChains

# py -m pytest -v --driver Chrome --driver-path chromedriver.exe test_hobbii_login.py

# 1-3 Проверка окошка поиска

def test_search_box(web_browser):
    page = Main_Page(web_browser)
    assert page.search_input.is_presented()


def test_search_box_btn(web_browser):
    page = Main_Page(web_browser)
    assert page.search_input_btn.is_clickable()


def test_search_box_result(web_browser):
    page = Main_Page(web_browser)
    page.search_input_btn.click()
    assert page.get_current_url() == 'https://hobbii.com/product/search?search='


# 3-8 Проверка поиска товара

def test_search_product(web_browser):
    page = Main_Page(web_browser)
    page.search_input.send_keys('Alpaca')
    page.search_input_btn.click()
    page.search_product_cards.is_visible()
    for elem in page.search_product_cards.get_text():
        assert 'Alpaca' in elem


@pytest.mark.parametrize("locator", ["альпака",
                                     "3546", "$%^&"])

def test_search_invalid_name_product(web_browser, locator):
    page = Main_Page(web_browser)
    page.search_input.send_keys(locator)
    page.wait_page_loaded()
    assert page.invalid_result.is_presented()


def test_add_to_cart(web_browser):
    page = Main_Page(web_browser)
    page.search_input.send_keys("Alpaca")
    page.search_input_btn.click()
    page.wait_page_loaded()

    page.search_product_cards_one.click()
    page.wait_page_loaded()

    page.desired_product_color.click()
    page.add_to_cart_btn.click()
    page.cart_box.click()
    page.wait_page_loaded()
    assert page.cart_banner.is_presented()


def test_add_to_cart_result(web_browser):
    page = Main_Page(web_browser)
    page.search_input.send_keys("Alpaca")
    page.search_input_btn.click()
    page.wait_page_loaded()
    #page.search_product_cards_one.is_visible()
    page.search_product_cards_one.click()
    page.wait_page_loaded()
    #page.desired_product_card.is_visible()
    page.desired_product_color.click()
    page.add_to_cart_btn.click()
    page.cart_box.click()
    page.wait_page_loaded()
    assert page.result_list.count() > 0

# 9 Проверка окошка сортировки по ...

def test_sort_by_btn_clickable(web_browser):
    page = Main_Page(web_browser)
    page.gen_menu_yarn.click()
    page.wait_page_loaded()
    assert page.sort_by_btn.is_clickable()


# 10-12 Сортировка по дате появления

def test_search_sort_by_date_old(web_browser):
    page = Main_Page(web_browser)
    page.gen_menu_yarn.click()
    page.wait_page_loaded()
    page.sort_by_btn.click()
    page.date_old.click()
    page.wait_page_loaded()
    page.screenshot("sort_by_date_old.png")


def test_search_sort_by_date_new(web_browser):
    page = Main_Page(web_browser)
    page.gen_menu_yarn.click()
    page.wait_page_loaded()
    page.sort_by_btn.click()
    page.date_new.click()
    page.wait_page_loaded()
    page.screenshot("sort_by_date_new.png")


# 13 Сортировка по возрастанию цены

def test_search_sort_by_price_low(web_browser):
    page = Main_Page(web_browser)
    page.gen_menu_yarn.click()
    page.wait_page_loaded()
    page.sort_by_btn.click()
    page.price_low.click()
    page.wait_page_loaded()
    page.screenshot("sort_by_price_low.png")


# 14 Сортировка по убыванию цены

def test_search_sort_by_price_high(web_browser):
    page = Main_Page(web_browser)
    page.gen_menu_yarn.click()
    page.wait_page_loaded()
    page.sort_by_btn.click()
    page.price_high.click()
    page.wait_page_loaded()
    page.screenshot("sort_by_price_high.png")


# 15 Сортировка по популярности товара

def test_search_sort_by_most_popular(web_browser):
    page = Main_Page(web_browser)
    page.gen_menu_yarn.click()
    page.wait_page_loaded()
    page.sort_by_btn.click()
    page.most_popular.click()
    page.wait_page_loaded()
    page.screenshot("sort_by_most_popular.png")







#XXXXX Меню Мой профиль
@pytest.mark.parametrize("locator", [Main_Page.gen_menu_home, Main_Page.gen_menu_yarn
                                     ])
def test_main_my_profile_menu(web_browser, locator):
    page = Main_Page(web_browser)
    page.find_element_by_xpath(locator).click()
    page.general_logo.click()
    assert page.get_current_url() == 'https://hobbii.com/'


def test_check_product_can_be_added_to_cart(web_browser):
    page = MainPage(web_browser)

    page.search = 'keyboard'
    page.search_run_button.click()

    page.results_list_titles[0].click()

    page.detail_add_to_card_button.click()

    assert page.detail_card_count.get_text() == '1'


def test_detail_page_contains_buy_button(web_browser):
    page = MainPage(web_browser)

    page.search = 'keyboard'
    page.search_run_button.click()

    page.results_list_titles[0].click()

    assert page.detail_buy_now_button.is_visible()
    assert page.detail_buy_now_button.is_clickable()


def test_detail_page_buy_button_click_redirects_to_signin(web_browser):
    page = MainPage(web_browser)

    page.search = 'keyboard'
    page.search_run_button.click()

    page.results_list_titles[0].click()

    page.detail_buy_now_button.click()
    page.wait_page_loaded()

    assert page.get_current_url().find("signin") != -1


def test_detail_page_contains_similar_items(web_browser):
    page = MainPage(web_browser)

    page.search = 'keyboard'
    page.search_run_button.click()

    page.results_list_titles[0].click()

    assert page.detail_similar_item.count() > 1


def test_detail_page_contains_related_items(web_browser):
    page = MainPage(web_browser)

    page.search = 'keyboard'
    page.search_run_button.click()

    page.results_list_titles[0].click()

    assert page.detail_related_products.count() > 1


def test_detail_page_contains_customer_questions_section(web_browser):
    page = MainPage(web_browser)

    page.search = 'keyboard'
    page.search_run_button.click()

    page.results_list_titles[0].click()

    assert page.detail_customer_questions.get_text().contains('Customer questions & answers')


def test_detail_page_contains_different_buy_options(web_browser):
    page = MainPage(web_browser)

    page.search = 'keyboard'
    page.search_run_button.click()

    page.results_list_titles[0].click()

    assert page.detail_buy_variants.count() > 1


