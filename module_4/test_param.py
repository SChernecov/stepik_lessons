from selenium import webdriver
import pytest
import time
import math

answer = math.log(int(time.time()))


@pytest.fixture(scope="module")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.parametrize('lessons', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_openned_lessons(browser, lessons):
    link = f"https://stepik.org/lesson/{lessons}/step/1"
    browser.get(link)

    input_file = browser.find_element_by_css_selector('.ember-text-area')
    input_file.send_keys(str(answer))

    send_button = browser.find_element_by_css_selector('.submit-submission')
    send_button.click()

    feedback_field = browser.find_element_by_css_selector('.smart-hints__hint')
    feedback_field_text = feedback_field.text
    assert feedback_field_text == 'Correct', 'Feedback field is incorrect!'
