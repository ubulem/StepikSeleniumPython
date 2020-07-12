from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, 'button[type="submit"][value="Add to basket"]')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_TITLE = (By.CSS_SELECTOR, '.product_main h1')
    BASKET_MESSAGE = (By.CSS_SELECTOR, '#messages>div:nth-child(1) strong')
    BASKET_PRICE = (By.CSS_SELECTOR, '#messages>div:nth-child(3) strong')
