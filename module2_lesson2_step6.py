from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    #функция, решающее выражание
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    #cчитываем значение для переменной х
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    #присваиваем переменной y значение выражения.
    y = calc(x)
    #вводим ответ в текстовое поле
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    #Отмечаем Checkbox
    option1 = browser.find_element_by_id('robotCheckbox')
    option1.click()
    #скроллим станицу вниз и выбираем radiobutton
    option2 = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()
    assert True
    #находим кнопку submit и нажимаем её
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
