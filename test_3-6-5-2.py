from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_c
from selenium import webdriver
import time
import math
import pytest

# для старта pytest -v -s 3_6_3_step_OWLS_OvO.py
# s, чтоб видеть print
# v, для того, чтобы запустить расширенный визуальный режим

uncorrected_results = []

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.implicitly_wait(55)
    yield browser
    print("\nquit browser..")
    browser.quit()
    print(''.join(uncorrected_results))

@pytest.mark.parametrize('link_task', ["236897", "236898"])
def test_find_ufo(browser, link_task):
    link = f"https://stepik.org/lesson/{link_task}/step/1"
    browser.get(link)
    button = browser.find_element(By.CLASS_NAME,
                                  'ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button')
    button.click()
    input1 = browser.find_element(By.NAME, 'login')
    input1.send_keys("victoriashevkunova@gmail.com")
    input2 = browser.find_element(By.NAME, "password")
    input2.send_keys("1047995Na")
    button32 = browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader")
    button32.click()
    answer_place = WebDriverWait(browser, 55) \
        .until(e_c.visibility_of_element_located((By.CSS_SELECTOR, '[placeholder="Напишите ваш ответ здесь..."]')))
    answer_place.send_keys(str(math.log(int(time.time()))))

    submit_button = WebDriverWait(browser, 55) \
        .until(e_c.visibility_of_element_located((By.CSS_SELECTOR, '[class="submit-submission"]')))
    submit_button.click()

    option_text = WebDriverWait(browser, 55) \
        .until(e_c.visibility_of_element_located((By.CSS_SELECTOR, '[class="smart-hints__hint"]'))).text

    if option_text != "Correct!":
        uncorrected_results.append(option_text)

    assert "Correct!" == option_text, f'Error: {option_text}'

