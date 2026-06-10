import pytest


def test_change_pricelist_to_eur(category_page):
    category_page.change_currency_to_eur()
    category_page.should_all_prices_be_in_eur()

def test_open_product_page(category_page):
    category_page.verify_product_name_in_source('Customizable Desk')
    category_page.open_first_product()

def test_filter_list_and_add_to_cart(category_page):
    category_page.switch_to_list_view()
    category_page.select_steel_filter()
    category_page.click_cart_icon()
    category_page.proceed_to_checkout()
    category_page.should_be_on_cart_page()
    category_page.verify_product_in_cart(
        'Customizable Desk (Steel, White)',
        '160x80cm, with large legs.'
    )
