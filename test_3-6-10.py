from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/"


def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    button = browser.find_elements(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    assert button, 'No button'
    time.sleep(10)

