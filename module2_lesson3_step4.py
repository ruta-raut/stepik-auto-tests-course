from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # function:
    def calc_lesson_formula(arg):
        return str(math.log(abs(12 * math.sin(int(arg)))))

    # click on the button
    button1 = browser.find_element_by_css_selector("button.btn")
    button1.click()
    # agree in modal window
    confirm = browser.switch_to.alert
    confirm.accept()
    # find the value x and assign the variable y the value of the expression
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc_lesson_formula(x)
    # input value of the expression
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    # click on the button "Submit"
    button2 = browser.find_element_by_css_selector("button.btn")
    button2.click()

finally:
    time.sleep(10)
    browser.quit()
