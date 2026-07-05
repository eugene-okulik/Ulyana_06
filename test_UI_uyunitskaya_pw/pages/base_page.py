class BasePage:

    base_url = "http://testshop.qa-practice.com/"

    def __init__(self, page):
        self.page = page

    def open(self, url):
        self.page.goto(url)

    def open_page(self):
        self.page.goto(self.base_url)

    def find(self, locator):
        return self.page.locator(locator)

    def click(self, locator):
        self.page.locator(locator).click()

    def get_text(self, locator):
        return self.page.locator(locator).text_content()

    def get_attribute(self, locator, attr):
        return self.page.locator(locator).get_attribute(attr)

    def hover(self, locator):
        self.page.locator(locator).hover()
