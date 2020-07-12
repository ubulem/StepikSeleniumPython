import pytest

from pages.product_page import ProductPage

url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'


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
