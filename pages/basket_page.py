from .base_page import *


class BasketPage(BasePage):

    def text_basket_is_empty(self):
        basket_text = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_TEXT)
        assert basket_text, "Didn't get message basket is empty"

    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Items in busket are presented, but should not be"