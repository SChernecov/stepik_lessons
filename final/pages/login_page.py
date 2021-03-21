from final.pages.base_page import BasePage
from final.pages.locators import LoginPageLocators
from final.pages.locators import ResetPasswordLocators
from final.pages.locators import BasePageLocators
from final.pages.locators import MainPageLocators
from final.pages.locators import SearchLocators

link = "http://selenium1py.pythonanywhere.com/accounts/login/"


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url.endswith("/accounts/login/")

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_LOCATOR), "Login email locator is not presented"
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_PASSWORD_LOCATOR), "Login password locator is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_EMAIL_LOCATOR), "Registration email locator is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_PASSWORD_LOCATOR), "Registration password locator is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REPEAT_REGISTRATION_EMAIL_LOCATOR), "Repeat registration password locator is not presented"

    def should_be_login_in(self):
        assert self.is_element_present(
            *BasePageLocators.MESSAGE_ABOUT_SUCCESS_LOGIN_IN_LOCATOR), "Successful sign in message is not displayed"

    def should_not_be_login_in(self):
        assert self.is_not_element_present(
            *BasePageLocators.MESSAGE_ABOUT_SUCCESS_LOGIN_IN_LOCATOR), "Successful sign in message is displayed"

    def switch_to_active_window(self):
        self.browser.actie_handles()

    def should_be_forgotten_password_form(self):
        assert self.is_element_present(
            *ResetPasswordLocators.RESET_EMAIL_LOCATOR), "Reset email field is not displayed"
        assert self.is_element_present(
            *ResetPasswordLocators.RESET_BUTTON_LOCATOR), "Reset button is not displayed"

    def should_be_search_title(self):
        assert self.is_element_present(*SearchLocators.SEARCH_TITLE_LOCATOR)
        assert self.is_not_element_present(*SearchLocators.SORT_BY_LIST_LOCATOR)

    def register_new_user(self, email, password):
        self.put_into(*LoginPageLocators.REGISTRATION_EMAIL_LOCATOR, email)
        self.put_into(*LoginPageLocators.REGISTRATION_PASSWORD_LOCATOR, password)
        self.put_into(*LoginPageLocators.REPEAT_REGISTRATION_EMAIL_LOCATOR, password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON_LOCATOR).click()

    def login_with_correct_data(self, email, password):
        self.put_into(*LoginPageLocators.LOGIN_EMAIL_LOCATOR, email)
        self.put_into(*LoginPageLocators.LOGIN_PASSWORD_LOCATOR, password)
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON_LOCATOR).click()

    def go_to_reset_password_page(self):
        self.browser.find_element(*LoginPageLocators.FORGOTTEN_PASSWORD_LINK_LOCATOR).click()

    def go_to_search_page(self):
        self.browser.find_element(*MainPageLocators.SEARCH_BASKET).click()
