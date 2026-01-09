from .base_page import BasePage

class ProductsPage(BasePage):
    def is_loaded(self):
        # SauceDemo Products page has a span with class 'title' and text 'Products'
        return self.page.locator(".title", has_text="Products").is_visible()