from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "//input[contains(@name, 'lastname') and @required]")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "//input[contains(@name, 'email') and @required]")
    input3.send_keys("1@gmail.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_1.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

