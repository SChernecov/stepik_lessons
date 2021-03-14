import pytest

from module_5.pages.product_page import ProductPage

class TestProductPage:
    @pytest.mark.parametrize('promo_offer',
                             ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6", "offer7", "offer8",
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
