import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en-GB", help="Choose language: ru, en-GB, es, fr")


@pytest.fixture
def language(request):
    return request.config.getoption("--language")


@pytest.fixture(scope="function")
def browser(language):
    # Задаем опции для запуска драйвера браузера
    options = Options()
    # Добавляем опцию intl.accept_languages
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    # Запускаем браузер Chrome и говорим чтобы использовал опции, которые мы опеределили выше
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
