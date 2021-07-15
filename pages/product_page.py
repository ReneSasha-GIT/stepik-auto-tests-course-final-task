from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def return_product_title(self):
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE)
        return product_title.text

    def return_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price.text

    def should_be_correct_add_title(self, product_title):
        add_title = self.browser.find_element(*ProductPageLocators.ADD_TITLE)
        assert add_title.text == product_title, f"Title in add-to-basket message is \"{add_title.text}\", but " \
                                                f"title on product page is \"{product_title}\""

    def should_be_correct_add_price(self, product_price):
        add_price = self.browser.find_element(*ProductPageLocators.ADD_PRICE)
        assert add_price.text == product_price, f"Price in add-to-basket message is \"{add_price.text}\", but " \
                                                f"price on product page is \"{product_price}\""

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_success_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should disappear"
