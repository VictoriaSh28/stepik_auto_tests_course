import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://stepik.org/lesson/236895/step/1"


@pytest.fixture(scope="class")
def browser():
    browser = webdriver.Firefox()
    browser.implicitly_wait(30)
    yield browser
    browser.quit()


class TestMainPage1():

    def test_find_button(self, browser):
        browser.get(link)
        button = browser.find_element(By.ID, "ember33")
        button.click()

        input1 = browser.find_element(By.ID, 'id_login_email')
        input1.send_keys("victoriashevkunova@gmail.com")
        input2 = browser.find_element(By.ID, "id_login_password")
        input2.send_keys("***")

        # Отправляем заполненную форму
        button = browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader")
        button.click()

    @pytest.mark.xfail(strict=True)
    def test_not_button(self, browser):
        browser.get(link)
        browser.find_element(By.ID, "ember33")




