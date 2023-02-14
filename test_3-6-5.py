import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Firefox()
    browser.implicitly_wait(30)
    yield browser
    browser.quit()


@pytest.mark.parametrize('link1', ['https://stepik.org/lesson/236897/step/1'
                            ])
class TestMainPage1:
    #
    # def test_find_button(self, browser):
    #     link = "https://stepik.org/lesson/236895/step/1"
    #     browser.get(link)
    #     button = browser.find_element(By.ID, "ember33")
    #     button.click()
    #     input1 = browser.find_element(By.ID, 'id_login_email')
    #     input1.send_keys("victoriashevkunova@gmail.com")
    #     input2 = browser.find_element(By.ID, "id_login_password")
    #     input2.send_keys("***")
    #
    #     # Отправляем заполненную форму
    #     button = browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader")
    #     button.click()

    def test_input(self, browser, link1):
        browser.implicity_wait(30)
        link = f'{link1}'
        browser.get(link)
        browser.implicity_wait(30)
        button = browser.find_element(By.CLASS_NAME, 'ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button')
        button.click()
        input1 = browser.find_element(By.NAME, 'login')
        input1.send_keys("victoriashevkunova@gmail.com")
        input2 = browser.find_element(By.NAME, "password")
        input2.send_keys("***")
        button32 = browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader")
        button32.click()
        WebDriverWait(browser, 30).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, 'ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button')))
        input3 = WebDriverWait(browser, 30).until(
            EC.visibility_of_element_located((By.TAG_NAME, 'textarea')))
        input3.send_keys(str(math.log(int(time.time() + 0.2))))
        button2 = WebDriverWait(browser, 30).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "submit-submission")))
        button2.click()
        browser.find_element(By.CLASS_NAME, "again-btn.white").click()
        browser.find_element(By.CSS_SELECTOR, "[data-ember-action-278='278']")
        input33 = browser.find_elements(By.TAG_NAME, 'textarea')
        input33.send_keys(str(math.log(int(time.time() + 0.2))))
        button22 = WebDriverWait(browser, 30).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "submit-submission")))
        button22.click()
        # browser.implicity_wait(30)
        input4 = WebDriverWait(browser, 30).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
        output = input4.text
        assert output == 'Correct!', 'Wrong message'
        # browser.implicity_wait(30)






