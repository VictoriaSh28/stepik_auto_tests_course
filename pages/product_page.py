from .base_page import *
from .locators import *


class ProductPage(BasePage):

    def add_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket.click()

    def test_page(self):
        title_1 = self.browser.find_element(*ProductPageLocators.BOOK_TITLE)
        title = title_1.text
        price_1 = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        price = price_1.text
        title_in_basket_1 = self.browser.find_element(*ProductPageLocators.TITLE_IN_BASKET)
        title_in_basket = title_in_basket_1.text
        price_in_basket_1 = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)
        price_in_basket = price_in_basket_1.text
        assert title == title_in_basket, 'Название не совпадает'
        assert price == price_in_basket, 'Цена не совпадает'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should disappear"




