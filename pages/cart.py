from playwright.sync_api import Page


class Cart_Page:
    TITLE = '[data-test="title"]'
    ITEMS = '[data-test="inventory-item"]'
    PRODUCT_NAME = '[data-test="inventory-item-name"]'
    PRODUCT_PRICE = '[data-test="inventory-item-price"]'
    ITEM_QUANTITY = '[data-test="item-quantity"]'
    BUTTON_CHECKOUT = '[data-test="checkout"]'

    def __init__(self, page: Page, variables):
        self.page = page
        self.variables = variables
        self.url = f"{self.variables['base_url']}/cart.html"

    def item_by_name(self, name: str):
        return self.page.locator(self.ITEMS).filter(has=self.page.get_by_text(name, exact=True))

    def start_checkout(self):
        self.page.locator(self.BUTTON_CHECKOUT).click()
