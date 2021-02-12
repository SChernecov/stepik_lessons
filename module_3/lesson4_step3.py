import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

try:
    browser = webdriver.Chrome()
    # переход на страницу
    browser.get('http://suninjuly.github.io/selects1.html')

    # находим элемент x
    x = browser.find_element_by_css_selector('#num1').text
    # находим элемент y
    y = browser.find_element_by_css_selector('#num2').text
    # считаем сумму заданных чисел
    summary = str(int(x) + int(y))
    print(summary)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(summary)

    browser.find_element_by_css_selector('button').click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
