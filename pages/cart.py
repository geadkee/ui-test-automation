from playwright.sync_api import Page, expect
from test_data.scenario_data import PRODUCTS
from utils.logger import log

class Cart_Page:
    TITLE = 'span[data-test="title"]'
    LABEL_QUANTITY = '[data-test="cart-quantity-label"]'
    LABEL_CART_DESC = '[data-test="cart-desc-label"]'
    ITEM = '[data-test="inventory-item"]'
    PRODUCT_NAME = '[data-test="inventory-item-name"]'
    PRODUCT_PRICE = '[data-test="inventory-item-price"]'
    ITEM_QUANTITY = '[data-test="item-quantity"]'
    BUTTON_REMOVE_ITEM = '[data-test="remove-{}"]'

    BUTTON_BACK_SHOPPING = 'button[data-test="continue-shopping"]'
    BUTTON_CHECKOUT = 'button[data-test="checkout"]'

    def __init__(self, page: Page, variables: dict):
        self.page = page
        self.variables = variables
        self.url = f"{self.variables['base_url'].rstrip('/')}/cart.html"

    def assert_cart_page(self):
        
        expect(self.page).to_have_url(self.url)
        expect(self.page.locator(self.TITLE)).to_have_text("Your Cart")
        expect(self.page.locator(self.LABEL_QUANTITY)).to_have_text("QTY")
        expect(self.page.locator(self.LABEL_CART_DESC)).to_have_text("Description")

        expect(self.page.locator(self.BUTTON_BACK_SHOPPING)).to_be_enabled()
        expect(self.page.locator(self.BUTTON_CHECKOUT)).to_be_enabled()

    def assert_cart_items(self, chosen_items: dict):
        
        expect(self.page.locator(self.ITEM)).to_have_count(len(chosen_items))

        for index, item_code in enumerate(chosen_items):
            item = self.page.locator(self.ITEM).nth(index)
            actual_item = item.inner_text()
            expected_item = PRODUCTS[item_code]

            log(f"Assert product's name, decription, price: '{actual_item}'")
            expect(self.page.locator(self.ITEM_QUANTITY).nth(index)).to_have_text("1")
            assert expected_item["name"] in actual_item, (f"Expected product name '{expected_item['name']}'")
            assert expected_item["description"] in actual_item, (f"Incorrect description for '{expected_item['name']}'")
            assert expected_item["price"] in actual_item, (f"Expected price '{expected_item['price']}' for '{expected_item['name']}'")

            expect(self.page.locator(self.BUTTON_REMOVE_ITEM.format(item_code))).to_be_enabled
            expect(self.page.locator(self.BUTTON_REMOVE_ITEM.format(item_code))).to_have_text("Remove")

    def go_to_checkout(self):
        self.page.locator(self.BUTTON_CHECKOUT).click()
