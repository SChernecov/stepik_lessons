from module_5.pages.base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCTS_LOCATOR), "Products is presented, but should not be"

    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE_LOCATOR), "Success message is not presented, but should be"