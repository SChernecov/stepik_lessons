def test_add_book_button_ru(browser, language):
    # Data
    book_page_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    add_book_button_locator = ".btn-primary"
    # Act
    browser.get(book_page_link)
    # Assert
    add_book_button = browser.find_element_by_css_selector(add_book_button_locator)
    add_book_button_text = add_book_button.text
    if language == "ru":
        assert add_book_button_text == 'Добавить в корзину', 'Не отображается текст кнопки "Добавить в корзину"'
    elif language == "en-GB":
        assert add_book_button_text == 'Add to basket', 'Не отображается текст кнопки "Add to basket"'
    elif language == "es":
        assert add_book_button_text == 'Añadir al carrito', 'Не отображается текст кнопки "Añadir al carrito"'
    elif language == "fr":
        assert add_book_button_text == 'Ajouter au panier', 'Не отображается текст кнопки "Ajouter au panier"'
    else:
        pytest.skip(f"Unsupported language: {language}")
