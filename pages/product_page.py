from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    product_title = None
    product_price = None

    def add_product_to_basket(self):
        self.product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
        self.solve_quiz_and_get_code()

    def should_be_added_to_basket(self):
        basket_message = self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE).text
        assert self.product_title == basket_message, f"{basket_message} is added, but expected {self.product_title}"

    def should_be_same_price(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert self.product_price == basket_price, f"Basket price is {basket_price}, but expected {self.product_price}"
