from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def should_be_correct_add_title(self):
        add_title = self.browser.find_element(*ProductPageLocators.ADD_TITLE)
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE)
        assert add_title.text == product_title.text, f"Title in add-to-basket message is \"{add_title.text}\", but " \
                                                     f"title on product page is \"{product_title.text}\""

    def should_be_correct_add_price(self):
        add_price = self.browser.find_element(*ProductPageLocators.ADD_PRICE)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert add_price.text == product_price.text, f"Price in add-to-basket message is \"{add_price.text}\", but " \
                                                     f"price on product page is \"{product_price.text}\""
