from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #функция, решающее выражание
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    #находим значение x и присваиваем переменной y значение выражения.
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    #Вводим ответ в текстовое поле
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    #Отмечаем Checkbox
    option1 = browser.find_element_by_id('robotCheckbox')
    option1.click()
    #Выбираем radiobutton
    option2 = browser.find_element_by_id('robotsRule')
    option2.click()
    #Нажимаем Submit (отправляем заполненную форму)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
