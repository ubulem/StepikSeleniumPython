import pytest

from pages.product_page import ProductPage

url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
plain_url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear'


@pytest.mark.parametrize('link', [f"{url}0",
                                  f"{url}1",
                                  f"{url}2",
                                  f"{url}3",
                                  f"{url}4",
                                  f"{url}5",
                                  f"{url}6",
                                  pytest.param(f"{url}7", marks=pytest.mark.xfail),
                                  f"{url}8",
                                  f"{url}9"])
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_be_added_to_basket()
    product_page.should_be_same_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, plain_url)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, plain_url)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, plain_url)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_disappear()
