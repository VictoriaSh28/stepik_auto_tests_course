import pytest
from .pages.product_page import *
import time
from .pages.basket_page import *
from .pages.login_page import *

@pytest.mark.skip
@pytest.mark.parametrize('link1', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  pytest.param ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail)
                                  ])
def test_guest_can_add_product_to_basket(browser, link1):
    link = f'{link1}'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(15)
    page.test_page()
    time.sleep(5)
    # page.should_not_be_success_message()
    # page.should_disappear()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page_basket = BasketPage(browser, browser.current_url)
    page_basket.text_basket_is_empty()
    page_basket.basket_is_empty()


@pytest.mark.login_guest
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/'
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.register_new_user(password=str(12345678)+"Ab_C", email=str(time.time()) + "@fakemail.org")
        page.should_be_authorized_user()
        time.sleep(5)

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        # page.solve_quiz_and_get_code()
        time.sleep(10)
        page.test_page()
        time.sleep(5)
        # page.should_not_be_success_message()
        # page.should_disappear()

    # def test_register_page(self, browser):
    #     link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    #     page = LoginPage(browser, link)
    #     page.open()
    #     page.go_to_login_page()
    #     page.register_new_user()
    #     page.should_be_authorized_user()
    #     time.sleep(15)
