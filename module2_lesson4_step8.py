from selenium import webdriver
import math
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc_lesson_formula(arg):
        return str(math.log(abs(12 * math.sin(int(arg)))))

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )

    book = browser.find_element(By.ID, 'book')
    book.click()

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc_lesson_formula(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    submit = browser.find_element(By.ID, 'solve')
    submit.click()

finally:
    time.sleep(5)
    browser.quit()