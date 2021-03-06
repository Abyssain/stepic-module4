from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def should_be_add_to_basket_button(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_right_basket_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_text = product_price.text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        basket_price_text = basket_price.text
        assert product_price_text == basket_price_text, "Wrong basket price"

    def should_be_right_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_text = product_name.text
        name_in_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_ALERT)
        name_in_alert_text = name_in_alert.text

        assert product_name_text == name_in_alert_text, "Wrong name in basket"

    def should_not_present_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but not should be"

    def should_disappeared_succes_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Succes message is not disappeared"
