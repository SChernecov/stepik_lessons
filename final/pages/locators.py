from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    SEARCH_BASKET = (By.CSS_SELECTOR, "#id_q")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "[value='Search']")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK_LOCATOR = (By.CSS_SELECTOR, "span .btn-default:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    MESSAGE_ABOUT_SUCCESS_LOGIN_IN_LOCATOR = (By.CSS_SELECTOR, ".alert-success.fade > .alertinner.wicon")


class LoginPageLocators:
    LOGIN_EMAIL_LOCATOR = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_LOCATOR = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button[name='login_submit']")
    REGISTRATION_EMAIL_LOCATOR = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_LOCATOR = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button[name='registration_submit']")
    REPEAT_REGISTRATION_EMAIL_LOCATOR = (By.CSS_SELECTOR, "#id_registration-password2")
    FORGOTTEN_PASSWORD_LINK_LOCATOR = (By.CSS_SELECTOR, "#login_form a")


class ProductPageLocators:
    ADD_PRODUCT_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_LOCATOR = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_NAME_IN_MESSAGE_LOCATOR = (By.CSS_SELECTOR, "#messages > div:nth-child(1) strong")
    PRODUCT_PRICE_LOCATOR = (By.CSS_SELECTOR, "p.price_color")
    BASKET_PRICE_IN_MESSAGE_LOCATOR = (By.CSS_SELECTOR, ".alertinner > p > strong")
    SUCCESS_MESSAGE_LOCATOR = (By.CSS_SELECTOR, "#messages div:nth-of-type(1) .alertinner")
    REVIEW_LINK_LOCATOR = (By.CSS_SELECTOR, "section  a")
    REVIEW_TITLE_LOCATOR = (By.CSS_SELECTOR, "legend")
    REVIEW_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#write_review")
    PRODUCT_LINK_AFTER_SEARCH_LOCATOR = (By.CSS_SELECTOR, ":nth-child(1) > article > h3 > a")


class BasketPageLocators:
    BASKET_MESSAGE_LOCATOR = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_PRODUCTS_LOCATOR = (By.CSS_SELECTOR, "#basket_formset")


class ResetPasswordLocators:
    RESET_EMAIL_LOCATOR = (By.CSS_SELECTOR, "#id_email")
    RESET_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".btn-primary")


class SearchLocators:
    SEARCH_TITLE_LOCATOR = (By.CSS_SELECTOR, ".breadcrumb > li:nth-of-type(2)")
    SORT_BY_LIST_LOCATOR = (By.CSS_SELECTOR, ".control-label")
