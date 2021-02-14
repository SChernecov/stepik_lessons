import os

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')
browser.find_element_by_css_selector('[placeholder="Enter first name"]').send_keys('Sergey')
browser.find_element_by_css_selector('[placeholder="Enter last name"]').send_keys('Chernecov')
browser.find_element_by_css_selector('[placeholder="Enter email"]').send_keys('123@mail.ru')
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
browser.find_element_by_css_selector('[name="file"]').send_keys(file_path)
browser.find_element_by_css_selector('button.btn').click()
