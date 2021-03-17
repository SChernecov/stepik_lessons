import time

import pytest

from module_5.pages.product_page import ProductPage
from module_5.pages.basket_page import BasketPage
from module_5.pages.login_page import LoginPage

page_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
login_link = "http://selenium1py.pythonanywhere.com/accounts/login/"
base_page_link = "http://selenium1py.pythonanywhere.com"


class TestProductPage:
    @pytest.mark.parametrize('promo_offer',
                             ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                              pytest.param("offer7", marks=pytest.mark.xfail), "offer8",
                              "offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo_offer}"
        page = ProductPage(browser, link)

        page.open()
        product_name = page.get_product_name()
        product_price = page.get_product_price()
        page.click_add_to_basket_button()
        page.solve_quiz_and_get_code()

        page.should_be_product_adding(name=product_name, price=product_price)

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # Открываем страницу товара
        page = ProductPage(browser, page_link)
        page.open()
        # Добавляем товар в корзину
        page.click_add_to_basket_button()
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        page.should_not_success_message_is_displayed()

    def test_guest_cant_see_success_message(self, browser):
        # Открываем страницу товара
        page = ProductPage(browser, page_link)
        page.open()
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        page.should_not_success_message_is_displayed()

    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        # Открываем страницу товара
        page = ProductPage(browser, page_link)
        page.open()
        # Добавляем товар в корзину
        page.click_add_to_basket_button()
        # Проверяем, что нет сообщения об успехе с помощью is_disappeared
        page.should_be_success_message_is_dissapeared()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = BasketPage(browser, base_page_link)
        page.open()
        page.go_to_basket_page()
        page.should_not_be_products_in_basket()
        page.should_be_message_empty_basket()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "Remont2021!"
        page = LoginPage(browser, login_link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()


    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, page_link)

        page.open()
        product_name = page.get_product_name()
        product_price = page.get_product_price()
        page.click_add_to_basket_button()
        page.solve_quiz_and_get_code()

        page.should_be_product_adding(name=product_name, price=product_price)

    def test_user_cant_see_success_message(self, browser):
        # Открываем страницу товара
        page = ProductPage(browser, page_link)
        page.open()
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        page.should_not_success_message_is_displayed()
