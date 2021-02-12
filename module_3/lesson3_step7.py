import time
import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    # переход на страницу
    browser.get('http://suninjuly.github.io/get_attribute.html')

    # находим элемент
    treasure = browser.find_element_by_css_selector('#treasure')
    # считываем текст из тэга
    value = treasure.get_attribute('valuex')
    # считаем функцию
    calculate = calc(value)

    field = browser.find_element_by_css_selector('#answer').send_keys(calculate)
    checkbox = browser.find_element_by_css_selector('#robotCheckbox').click()
    radiobutton = browser.find_element_by_css_selector('#robotsRule').click()
    button = browser.find_element_by_css_selector('button').click()
    time.sleep(15)



finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
