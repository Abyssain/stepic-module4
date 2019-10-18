from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Login link is not found"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "There are not login form here"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "There are not registration form here"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FORM).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FORM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_FORM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_BUTTON).click()
