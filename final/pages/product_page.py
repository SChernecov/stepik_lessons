from final.pages.base_page import BasePage
from final.pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_basket_button(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_BUTTON_LOCATOR)
        link.click()

        # считываю название продукта

    def get_product_name(self):
        product_name = self.get_element_text(*ProductPageLocators.PRODUCT_NAME_LOCATOR)
        return product_name

        # считываю цену продукта

    def get_product_price(self):
        product_price = self.get_element_text(*ProductPageLocators.PRODUCT_PRICE_LOCATOR)
        return product_price

    def should_be_correct_product_adding(self, product_name):
        product_name_in_message = self.get_element_text(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE_LOCATOR)
        assert product_name == product_name_in_message, "The title of the book does not match the one added"

    def should_be_correct_price_basket(self, product_price):
        product_price_in_message = self.get_element_text(*ProductPageLocators.BASKET_PRICE_IN_MESSAGE_LOCATOR)
        assert product_price == product_price_in_message, "The value of the basket does not match the price of the item"

    def should_be_product_adding(self, name, price):
        self.should_be_correct_product_adding(name)
        self.should_be_correct_price_basket(price)

    def should_not_success_message_is_displayed(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE_LOCATOR), "Success message is presented, but should not be"

    def should_be_success_message_is_disappeared(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE_LOCATOR), "Success message is presented, but should not be"
