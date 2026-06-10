import pytest
from playwright.sync_api import sync_playwright
from pages.cart_page import CartPage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage


@pytest.fixture()
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

@pytest.fixture()
def cart_page(page):
    page_obj = CartPage(page)
    page_obj.open_page()
    return page_obj

@pytest.fixture()
def category_page(page):
    page_obj = CategoryPage(page)
    page_obj.open_page()
    return page_obj

@pytest.fixture()
def product_page(page):
    page_obj = ProductPage(page)
    page_obj.open_page()
    return page_obj
