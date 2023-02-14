import time

from .base_page import BasePage
from .locators import *


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = str(self.browser.current_url)
        assert 'login' in current_url, "Login is not in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, password, email):
        input1 = self.browser.find_element(*LoginPageLocators.EMAIL_REG)
        input1.send_keys(email)
        input2 = self.browser.find_element(*LoginPageLocators.PASSWORD_REG)
        input2.send_keys(password)
        input3 = self.browser.find_element(*LoginPageLocators.PASSWORD_REG_CONFIRM)
        input3.send_keys(password)

        # Отправляем заполненную форму
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()
