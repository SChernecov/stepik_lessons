from selenium import webdriver
from sys import argv

# Задаем в скрипте параметры
script_name, link = argv

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_css_selector("[placeholder='Input your first name']")
    first_name.send_keys("Sergey")
    last_name = browser.find_element_by_css_selector("[placeholder='Input your last name']")
    last_name.send_keys("Chernecov")
    email = browser.find_element_by_css_selector("[placeholder='Input your email']")
    email.send_keys("my@mail.ru")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
