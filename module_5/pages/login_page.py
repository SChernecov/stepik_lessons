from module_5.pages.base_page import BasePage
from .locators import LoginPageLocators

link = "http://selenium1py.pythonanywhere.com/accounts/login/"


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url == link

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_LOCATOR), "Login email locator is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_LOCATOR), "Login password locator is not presented"


    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL_LOCATOR), "Registration email locator is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_LOCATOR), "Registration password locator is not presented"
        assert self.is_element_present(*LoginPageLocators.REPEAT_REGISTRATION_EMAIL_LOCATOR), "Repeat registration password locator is not presented"
