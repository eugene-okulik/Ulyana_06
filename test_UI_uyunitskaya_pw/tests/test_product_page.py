import pytest


def test_breadcrumb_multimedia(product_page):
    product_page.check_breadcrumb('Multimedia')

def test_quantity_adjustment_and_cart_sync(product_page):
    product_page.click_plus_multi(10)
    product_page.add_to_cart()
    product_page.view_cart()
    product_page.decrease_quantity_in_cart()
    product_page.check_quantity_in_cart(10)

def test_add_and_remove_from_cart(product_page):
    product_page.add_to_cart()
    product_page.go_to_cart_via_header()
    product_page.remove_item_from_cart()
    product_page.should_be_empty_cart()
