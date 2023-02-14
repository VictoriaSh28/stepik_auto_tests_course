from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


def calc(x1, x2):
    return str(int(x1) + int(x2))


try:
    link = " https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_1_0 = browser.find_element(By.ID, 'num1')
    x1 = x_1_0.text
    x_2_0 = browser.find_element(By.ID, 'num2')
    x2 = x_2_0.text

    y = calc(x1, x2)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(y)

    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()