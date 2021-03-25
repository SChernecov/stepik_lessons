import pytest

from final.pages.product_page import ProductPage

page_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
login_link = "http://selenium1py.pythonanywhere.com/accounts/login/"
base_page_link = "http://selenium1py.pythonanywhere.com"


class TestProductPage:
    @pytest.mark.personal_test
    def test_guest_can_open_product_review_form_with_link(self, browser):
        # Arrange
        page = ProductPage(browser, page_link)
        page.open()

        # Act
        page.open_review_form_with_link()

        # Assert
        page.should_be_correct_review_form()

    @pytest.mark.personal_test
    def test_guest_can_open_product_review_form_with_button(self, browser):
        # Arrange
        page = ProductPage(browser, page_link)
        page.open()

        # Act
        page.open_review_form_with_button()

        # Assert
        page.should_be_correct_review_form()

    @pytest.mark.personal_test
    @pytest.mark.parametrize('product_name',
                             ["The Rspec Book", "Oscar T-shirt"])
    def test_guest_can_find_product_by_name(self, browser, product_name):
        # Arrange
        page = ProductPage(browser, page_link)
        page.open()

        # Act
        page.search_product_by_name(product_name)
        page.open_found_product()

        # Assert
        page.should_be_correct_product_found(product_name)
