add_book_button_locator = ".btn-primary"


def test_add_book_button_ru(browser, language):
    # Data
    book_page_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    button_values_options = {"ru": 'Добавить в корзину', "en-GB": 'Add to basket', "es": 'Añadir al carrito',
                             "fr": 'Ajouter au panier'}

    # Act
    browser.get(book_page_link)
    add_book_button = browser.find_element_by_css_selector(add_book_button_locator)
    add_book_button_text = add_book_button.text
    # Assert
    assert add_book_button_text == button_values_options[language]
