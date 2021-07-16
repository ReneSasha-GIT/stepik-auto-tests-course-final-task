from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_fld = self.browser.find_element(*LoginPageLocators.EMAIL_REG)
        email_fld.send_keys(email)
        pass1_fld = self.browser.find_element(*LoginPageLocators.PASSWORD_1_REG)
        pass1_fld.send_keys(password)
        pass2_fld = self.browser.find_element(*LoginPageLocators.PASSWORD_2_REG)
        pass2_fld.send_keys(password)
        reg_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        reg_btn.click()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "word \"login\" not in url"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
