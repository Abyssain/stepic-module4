from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.XPATH,"//div[@class='col-sm-6 product_main']/h1") #выьрать селекор для строки с названием товара
    PRODUCT_PRICE = (By.XPATH, "//div[@class='col-sm-6 product_main']/p[@class='price_color']")
    PRODUCT_NAME_IN_ALERT = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    BASKET_PRICE = (By.XPATH, "//div[@class='alertinner ']/p/strong")

    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]")
