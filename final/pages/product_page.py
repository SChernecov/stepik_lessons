from final.pages.base_page import BasePage
from final.pages.locators import ProductPageLocators
from final.pages.locators import MainPageLocators


class ProductPage(BasePage):
    def click_add_to_basket_button(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_BUTTON_LOCATOR)
        link.click()

    def get_product_name(self):
        product_name = self.get_element_text(*ProductPageLocators.PRODUCT_NAME_LOCATOR)
        return product_name

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

    def should_be_correct_review_form(self):
        assert self.is_element_present(
            *ProductPageLocators.REVIEW_TITLE_LOCATOR), "Review title is not presented, but should be"

    def open_review_form_with_link(self):
        self.browser.find_element(*ProductPageLocators.REVIEW_LINK_LOCATOR).click()

    def open_review_form_with_button(self):
        self.browser.find_element(*ProductPageLocators.REVIEW_BUTTON_LOCATOR).click()

    def should_be_search_result(self):
        self.should_be_correct_product_found()

    def search_product_by_name(self, product_name):
        self.put_into(*MainPageLocators.SEARCH_BASKET, product_name)
        self.browser.find_element(*MainPageLocators.SEARCH_BUTTON).click()

    def open_found_product(self):
        self.browser.find_element(*ProductPageLocators.PRODUCT_LINK_AFTER_SEARCH_LOCATOR).click()

    def should_be_correct_product_found(self, product_name):
        assert product_name == self.get_element_text(
            *ProductPageLocators.PRODUCT_NAME_LOCATOR), "Product name is different from the one found"
