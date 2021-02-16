import string
from random import choice
from selenium import webdriver

main_page_link = "http://selenium1py.pythonanywhere.com/ru/"

registration_link_locator = '#login_link'
registration_email_input_locator = '#id_registration-email'
password_input_locator = '#id_registration-password1'
repeat_password_input_locator = '#id_registration-password2'
registration_button_locator = '[name="registration_submit"]'
success_page_title_locator = '.alertinner.wicon'


def get_random_email():
    email_name = ''.join(choice(string.ascii_letters) for _ in range(5))
    return f"{email_name}@gmail.com"


def get_random_password():
    password = ''.join(choice(string.ascii_letters) for _ in range(9))
    return password


def test_registration():
    # Data
    user_email = get_random_email()
    user_password = get_random_password()
    success_registration_message = 'Спасибо за регистрацию!'

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)

        # Act
        registration_link = browser.find_element_by_css_selector(registration_link_locator)
        registration_link.click()

        registration_email_input = browser.find_element_by_css_selector(registration_email_input_locator)
        registration_email_input.send_keys(user_email)

        registration_password_input = browser.find_element_by_css_selector(password_input_locator)
        registration_password_input.send_keys(user_password)

        repeat_registration_password_input = browser.find_element_by_css_selector(repeat_password_input_locator)
        repeat_registration_password_input.send_keys(user_password)

        registration_button = browser.find_element_by_css_selector(registration_button_locator)
        registration_button.click()

        # Assert
        success_page_title = browser.find_element_by_css_selector(success_page_title_locator)
        success_page_title_text = success_page_title.text
        assert success_page_title_text == success_registration_message, 'The message about successful registration is not displayed'

    finally:
        browser.quit()


test_registration()
