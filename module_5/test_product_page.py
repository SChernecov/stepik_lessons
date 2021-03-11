from module_5.pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


class TestProductPage:
    def test_add_item_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.adding_book()
        page.solve_quiz_and_get_code()
        page.should_be_product_adding()
