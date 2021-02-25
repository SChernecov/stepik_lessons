import conftest.py

main_page_link = "http://selenium1py.pythonanywhere.com/ru/"

book_link_locator = "[title='Coders at Work']"
all_goods_locator = "[href='\/ru\/catalogue\/']"
add_book_button_locator = ".btn-primary"


@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_add_book_button_ru(browser):
    browser.get(main_page_link)
    all_goods = browser.find_element_by_css_selector(all_goods_locator)
    all_goods.click()
    book_link = browser.find_element_by_css_selector(book_link_locator)
    book_link.click()
    add_book_button = browser.find_element_by_css_selector(add_book_button_locator)
    add_book_button_text = add_book_button.text
    assert add_book_button_text == 'Добавить в корзину', 'Не отображается кнопка "Добавить в корзину"'


@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_add_book_button_com(browser):
    browser.get(main_page_link)
    all_goods = browser.find_element_by_css_selector(all_goods_locator)
    all_goods.click()
    book_link = browser.find_element_by_css_selector(book_link_locator)
    book_link.click()
    add_book_button = browser.find_element_by_css_selector(add_book_button_locator)
    add_book_button_text = add_book_button.text
    assert add_book_button_text == 'Добавить в корзину', 'Не отображается кнопка "Добавить в корзину"'
