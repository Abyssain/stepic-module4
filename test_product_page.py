from Pages.product_page import ProductPage
from Pages.basket_page import BasketPage
from Pages.login_page import LoginPage
from Pages.base_page import BasePage
import time
import pytest

@pytest.mark.with_reg
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse = True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page_login = LoginPage(browser, link)
        page_login.open()
        page_login.register_new_user(email, password)
        page_base = BasePage(browser, link)
        page_base.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_present_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket_button()
        page.should_be_right_basket_price()
        page.should_be_right_product_name()


class TestAddToBasket():
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket_button()
        page.should_be_right_basket_price()
        page.should_be_right_product_name()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket_button()
        page.should_not_present_success_message()


    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket_button()
        page.should_disappeared_succes_message()


class TestLoginPage():
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
        
    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page (self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

@pytest.mark.empty_basket
class TestEmptyBasket():
    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty_basket()
        basket_page.should_be_message_about_empty_basket()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty_basket()
        basket_page.should_be_message_about_empty_basket()
