import math

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
# переходим на страницу
browser.get('http://SunInJuly.github.io/execute_script.html')
# находим переменную x
x = browser.find_element_by_id('input_value').text
calculate = calc(x)
browser.execute_script("window.scrollBy(0, 100);")
field = browser.find_element_by_id('answer').send_keys(calculate)
check_box = browser.find_element_by_id('robotCheckbox').click()
radio_button = browser.find_element_by_css_selector('[for="robotsRule"]').click()
button = browser.find_element_by_tag_name("button").click()

