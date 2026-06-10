import pytest


def test_cart_header_and_empty_state(cart_page):
    cart_page.should_be_correct_header('Order overview')
    cart_page.should_be_empty_cart_message('Your cart is empty!')

def test_categories_tabs_navigation(cart_page):
    cart_page.open_desks_in_new_tab()
    cart_page.verify_url_contains('desks')
    cart_page.close_tab_and_return()
    cart_page.open_furn_in_new_tab()
    cart_page.verify_url_contains('furnitures')
    cart_page.close_tab_and_return()
    cart_page.should_be_correct_header('Order overview')

def test_contact_us_validation(cart_page):
    cart_page.click_contact_us()
    cart_page.click_submit()
    cart_page.should_be_validation_error('Please fill in the form correctly.')
