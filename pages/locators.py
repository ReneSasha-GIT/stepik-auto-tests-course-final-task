from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-default[href*=basket]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_REG = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_1_REG = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_2_REG = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class MainPageLocators:
    pass


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADD_TITLE = (By.CSS_SELECTOR, ".alertinner > strong")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main > h1")
    ADD_PRICE = (By.CSS_SELECTOR, ".alertinner > p > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-success")
