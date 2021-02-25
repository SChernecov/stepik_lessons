from selenium import webdriver
import pytest

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.mark.parametrize('language', ["ru", "en-gb"])


