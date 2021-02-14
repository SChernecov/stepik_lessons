import math

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')
browser.find_element_by_tag_name('button').click()
confirm = browser.switch_to.alert.accept()
x = browser.find_element_by_id('input_value').text
calculate = calc(x)
print(calculate)
browser.find_element_by_id('answer').send_keys(calculate)
browser.find_element_by_tag_name('button').click()
