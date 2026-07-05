from pages.base_page import BasePage
from pages.locators.category_locators import CategoryLocators


class CategoryPage(BasePage):

    def open_page(self):
        self.open(self.base_url + 'shop/category/desks-1')

    def verify_product_name_in_source(self, name):
        assert name in self.page.content()

    def open_first_product(self):
        self.page.locator(CategoryLocators.PRODUCT_NAME).first.click()

    def switch_to_list_view(self):
        self.page.locator(CategoryLocators.LIST_VIEW_BTN).click()
        self.page.wait_for_timeout(1000)

    def select_steel_filter(self):
        self.page.locator(CategoryLocators.STEEL_CHECKBOX).first.click(force=True)
        self.page.wait_for_timeout(1000)

    def click_cart_icon(self):
        self.page.locator(CategoryLocators.ADD_TO_CART_ICON).first.click(force=True)

    def proceed_to_checkout(self):
        self.page.goto(self.base_url + 'shop/cart')

    def should_be_on_cart_page(self):
        assert '/shop/cart' in self.page.url

    def verify_product_in_cart(self, full_name, description):
        assert self.page.locator('.js_cart_lines').is_visible()

    def change_currency_to_eur(self):
        self.click(CategoryLocators.PRICELIST_BTN)
        self.page.locator(CategoryLocators.EUR_PRICELIST).click()

    def should_all_prices_be_in_eur(self):
        assert '€' in self.page.content()
