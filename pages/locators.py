from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs .btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_REG = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_REG = (By.CSS_SELECTOR, '#id_registration-password1')
    PASSWORD_REG_CONFIRM = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[value="Register"]')


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    BOOK_TITLE = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    BOOK_PRICE = (By.XPATH, "//div[@class='col-sm-6 product_main']/p[@class='price_color']")
    TITLE_IN_BASKET = (By.XPATH, "//div[@class='alertinner ']/strong")
    PRICE_IN_BASKET = (By.XPATH, "//div[@class='alertinner ']/p/strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1) .alertinner")


class BasketPageLocators:
    BASKET_IS_EMPTY_TEXT = (By.XPATH, '//p[contains(text(), "Your basket is empty")]')
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')



