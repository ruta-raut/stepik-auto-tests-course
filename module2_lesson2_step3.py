from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #находим значение x и y присваиваем переменной c сумму переменных x и y.
    x_element = browser.find_element_by_id("num1")
    y_element = browser.find_element_by_id("num2")
    x = x_element.text
    y = y_element.text
    c = int(x) + int(y)
    #выбираем в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(c))
    #Нажимаем Submit (отправляем заполненную форму)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
