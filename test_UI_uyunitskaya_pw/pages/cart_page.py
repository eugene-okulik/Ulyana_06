from pages.base_page import BasePage
from pages.locators.cart_locators import CartLocators


class CartPage(BasePage):

    def open_page(self):
        self.open(self.base_url + 'shop/cart')

    def open_desks_in_new_tab(self):
        self.page.locator(
            CartLocators.CATEGORIES_MENU
        ).first.hover()
        with self.page.context.expect_page() as new_page:
            self.page.locator(
                CartLocators.DESKS_LINK
            ).first.click(button='middle')
        self.new_page = new_page.value

    def open_furn_in_new_tab(self):
        self.page.locator(
            CartLocators.CATEGORIES_MENU
        ).first.hover()
        with self.page.context.expect_page() as new_page:
            self.page.locator(
                CartLocators.FURN_LINK
            ).first.click(button='middle')
        self.new_page = new_page.value

    def close_tab_and_return(self):
        self.new_page.close()

    def verify_url_contains(self, word):
        assert word in self.new_page.url

    def should_be_correct_header(self, expected_text):
        actual_text = self.get_text(CartLocators.HEADER)
        assert expected_text in actual_text

    def should_be_empty_cart_message(self, expected_text):
        assert expected_text in self.page.content()

    def click_contact_us(self):
        self.page.locator(CartLocators.CONTACT_BTN).first.click()

    def click_submit(self):
        self.page.locator(CartLocators.SUBMIT_BTN).click(force=True)

    def should_be_validation_error(self, expected_text):
        assert self.page.locator('#contactus_form').is_visible()

    def open_search(self):
        self.click(CartLocators.SEARCH_BTN)

    def should_be_warning_text(self, expected_text):
        actual_text = self.get_text(CartLocators.WARNING)
        assert expected_text in actual_text
