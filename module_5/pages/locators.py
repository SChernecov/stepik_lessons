from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_EMAIL_LOCATOR = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_LOCATOR = (By.CSS_SELECTOR, "#id_login-password")
    REGISTRATION_EMAIL_LOCATOR = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_LOCATOR = (By.CSS_SELECTOR, "#id_registration-password1")
    REPEAT_REGISTRATION_EMAIL_LOCATOR = (By.CSS_SELECTOR, "#id_registration-password2")

class ProductPageLocators():
    ADD_PRODUCT_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_LOCATOR = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_NAME_IN_MESSAGE_LOCATOR = (By.CSS_SELECTOR, "#messages > div:nth-child(1) strong")
    PRODUCT_PRICE_LOCATOR = (By.CSS_SELECTOR, "p.price_color")
    BASKET_PRICE_IN_MESSAGE_LOCATOR = (By.CSS_SELECTOR, ".alertinner > p > strong")
    SUCCESS_MESSAGE_LOCATOR = (By.CSS_SELECTOR, "#messages div:nth-of-type(1) .alertinner")
