import pytest
from module_5.pages.main_page import MainPage
from module_5.pages.basket_page import BasketPage
from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.login_guest
class TestMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        # Arrange
        page = MainPage(browser, link)
        page.open()

        # Act
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)

        # Assert
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        # Arrange
        page = MainPage(browser, link)

        # Act
        page.open()

        # Assert
        page.should_be_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        # Arrange
        page = BasketPage(browser, link)
        page.open()

        # Act
        page.go_to_basket_page()

        # Assert
        page.should_not_be_products_in_basket()
        page.should_be_message_empty_basket()