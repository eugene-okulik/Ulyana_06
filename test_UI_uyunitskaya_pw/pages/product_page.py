from pages.base_page import BasePage
from pages.locators.product_locators import ProductLocators


class ProductPage(BasePage):

    def open_page(self):
        self.open(self.base_url + 'shop/furn-9999-office-design-software-7?category=9')

    def check_breadcrumb(self, expected_text):
        actual_text = self.get_text(ProductLocators.BREADCRUMB)
        assert expected_text in actual_text

    def change_currency_to_eur(self):
        self.page.locator(ProductLocators.PRICELIST_BTN).click()
        self.page.locator(ProductLocators.EUR_PRICELIST).click()

    def click_plus_multi(self, times):
        for _ in range(times):
            self.page.locator(ProductLocators.PLUS_BTN).click()

    def add_to_cart(self):
        self.click(ProductLocators.ADD_TO_CART_BTN)
        self.page.wait_for_timeout(1000)

    def view_cart(self):
        self.page.goto(self.base_url + 'shop/cart')
        self.page.wait_for_timeout(1000)

    def decrease_quantity_in_cart(self):
        pass

    def check_quantity_in_cart(self, expected_qty):
        assert 'Order overview' in self.page.content()

    def go_to_cart_via_header(self):
        self.page.locator(ProductLocators.HEADER_CART_ICON).first.click(force=True)
        self.page.wait_for_timeout(1000)

    def remove_item_from_cart(self):
        self.page.locator(ProductLocators.REMOVE_ITEM_BTN).first.click(force=True)
        self.page.wait_for_timeout(1000)

    def should_be_empty_cart(self):
        assert 'Your cart is empty!' in self.page.content()
