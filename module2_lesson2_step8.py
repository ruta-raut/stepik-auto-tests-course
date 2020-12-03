from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #заполняем текстовые поля
    input1 = browser.find_element_by_name('firstname')
    input1.send_keys('Ruta')
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys('Filippova')
    input3 = browser.find_element_by_name('email')
    input3.send_keys('ruta.filippova')
    # получаем путь к директории текущего исполняемого файла 
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла 
    file_path = os.path.join(current_dir, 'file_for_module2_lesson2_step8.txt')
    #находим элемент для добавления файла и добавляем файл
    add_file = browser.find_element_by_id('file')
    add_file.send_keys(file_path)
    #находим кнопку submit и нажимаем её
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
    
