from module_5.pages.base_page import BasePage
from .locators import BasketPageLocators



class ProductPage(BasePage):
    def adding_book(self):
        link = self.browser.find_element(*BasketPageLocators.ADD_BOOK_BUTTON_LOCATOR)
        link.click()

    def should_be_product_adding(self):
        self.should_be_correct_product_adding()
        self.should_be_correct_price_basket()

    def should_be_correct_product_adding(self):
        assert self.text_attributes(*BasketPageLocators.BOOK_NAME_LOCATOR) == self.text_attributes(*BasketPageLocators.ADD_BOOK_NAME_LOCATOR)

    def should_be_correct_price_basket(self):
        assert self.text_attributes(*BasketPageLocators.BOOK_PRICE_LOCATOR) == self.text_attributes(*BasketPageLocators.MESSAGE_BASKET_PRICE_LOCATOR)
