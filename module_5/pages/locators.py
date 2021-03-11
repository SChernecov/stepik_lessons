from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_EMAIL_LOCATOR = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_LOCATOR = (By.CSS_SELECTOR, "#id_login-password")
    REGISTRATION_EMAIL_LOCATOR = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_LOCATOR = (By.CSS_SELECTOR, "#id_registration-password1")
    REPEAT_REGISTRATION_EMAIL_LOCATOR = (By.CSS_SELECTOR, "#id_registration-password2")

class BasketPageLocators():
    ADD_BOOK_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME_LOCATOR = (By.CSS_SELECTOR, "article h1")
    ADD_BOOK_NAME_LOCATOR = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    BOOK_PRICE_LOCATOR = (By.CSS_SELECTOR, "p.price_color")
    MESSAGE_BASKET_PRICE_LOCATOR = (By.CSS_SELECTOR, "#messages > div > div > p:nth-child(1) > strong")
