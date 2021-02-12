import time
import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    # переход на страницу
    browser.get('http://suninjuly.github.io/math.html')

    # находим элемент
    x_element = browser.find_element_by_css_selector('#input_value')
    # считываем текст из тэга
    x = x_element.text
    # считаем функцию
    y = calc(x)

    field = browser.find_element_by_css_selector('#answer').send_keys(y)
    checkbox = browser.find_element_by_css_selector('[for=robotCheckbox]').click()
    radiobutton = browser.find_element_by_css_selector('[for="robotsRule"]').click()
    button = browser.find_element_by_css_selector('button').click()
    time.sleep(15)



finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
