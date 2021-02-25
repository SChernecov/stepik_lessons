def test_add_book_button_ru(browser):
    # Data
    book_page_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    add_book_button_locator = ".btn-primary"
    value_book_button_attribut = "value"
    # Act
    browser.get(book_page_link)
    # Assert
    add_book_button = browser.find_element_by_css_selector(add_book_button_locator)
    add_book_button_text = add_book_button.text
    value_book_button = add_book_button.get_attribute(value_book_button_attribut)
    assert add_book_button_text == value_book_button, 'Не отображается кнопка "Добавить в корзину"'
