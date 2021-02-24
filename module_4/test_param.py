import time
import pytest
import math
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

answer = math.log(int(time.time()))


@pytest.fixture(scope="module")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize('lessons', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_open_lessons(browser, lessons):
    link = f"https://stepik.org/lesson/{lessons}/step/1"
    browser.get(link)

    input_file = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '.ember-text-area')))
    input_file.send_keys(str(answer))

    send_button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.submit-submission')))
    send_button.click()

    feedback_field = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint')))
    feedback_field_text = feedback_field.text
    assert feedback_field_text == 'Correct', 'Feedback field is incorrect!'
