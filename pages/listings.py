from playwright.sync_api import Page, expect
import random


class Listing_Page:
    TITLE = '[data-test="title"]'
    SORTING_VALUE = '[data-test="active-option"]'
    PRODUCT_CARDS = '[data-test="inventory-item"]'
    BUTTON_ADD_TO_CART = 'button[data-test^="add-to-cart-"]'
    CART_BADGE = '[data-test="shopping-cart-badge"]'
    LINK_CART = '[data-test="shopping-cart-link"]'

    PRODUCT_NAMES = '[data-test="inventory-item-name"]'

    PRODUCTS = {
        "sauce-labs-backpack": {
            "name": "Sauce Labs Backpack",
            "description": "Streamlined backpack with protective storage for a laptop and tablet.",
            "price": "29.99",
            "image_src": "https://www.saucedemo.com/assets/sauce-backpack-1200x1500-CjRW-Djj.jpg",
        },
        "sauce-labs-bike-light": {
            "name": "Sauce Labs Bike Light",
            "description": "Water-resistant red bicycle light with three modes and an included AAA battery.",
            "price": "9.99",
            "image_src": "https://www.saucedemo.com/assets/bike-light-1200x1500-DxcZRFOA.jpg",
        },
        "sauce-labs-bolt-t-shirt": {
            "name": "Sauce Labs Bolt T-Shirt",
            "description": "Gray cotton American Apparel shirt featuring a red lightning bolt.",
            "price": "15.99",
            "image_src": "https://www.saucedemo.com/assets/bolt-shirt-1200x1500-mR0ldpVS.jpg",
        },
        "sauce-labs-fleece-jacket": {
            "name": "Sauce Labs Fleece Jacket",
            "description": "Medium-weight fleece with a quarter-length zipper, suitable for outdoor and office wear.",
            "price": "49.99",
            "image_src": "https://www.saucedemo.com/assets/sauce-pullover-1200x1500-BfbI-PSd.jpg",
        },
        "sauce-labs-onesie": {
            "name": "Sauce Labs Onesie",
            "description": "Infant bodysuit with reinforced snap fasteners and durable stitched edges.",
            "price": "7.99",
            "image_src": "https://www.saucedemo.com/assets/red-onesie-1200x1500-BrSuq0ic.jpg",
        },
        "test.allthethings()-t-shirt-(red)": {
            "name": "Test.allTheThings() T-Shirt (Red)",
            "description": "Soft cotton red shirt with an automation-testing theme.",
            "price": "15.99",
            "image_src": "https://www.saucedemo.com/assets/red-tatt-1200x1500-E-qp6aYf.jpg",
        },
    }


    def __init__(self, page: Page):
        self.page = page
        # self.variables = variables
        self.url = "https://www.saucedemo.com/inventory.html"

    def wait_until_loaded(self):
        expect(self.page).to_have_url(self.url)
        expect(self.page.locator(self.TITLE)).to_have_text("Products")

    def assert_listings(self, is_valid_user: bool=True):

        if is_valid_user:
            expect(self.page).to_have_url(self.url)
            expect(self.page.locator(self.TITLE)).to_have_text("Products")
            expect(self.page.locator(self.PRODUCT_CARDS)).not_to_have_count(0)

            expect(self.page.locator(self.SORTING_VALUE)).to_have_text("Name (A to Z)")
            product_names = self.page.locator(self.PRODUCT_NAMES).all_text_contents()
            assert product_names == sorted(product_names), f"Product list is not sorted A to Z: {product_names}"
        else:
            print("Invalid user in listing page")


    def add_product_to_cart(self, name: str):
        product = self.page.locator(self.PRODUCT_CARDS).filter(
            has=self.page.get_by_text(name, exact=True)
        )
        product.locator(self.BUTTON_ADD_TO_CART).click()

        for product_key, product in PRODUCTS.items():
            self.page.locator(
                f'[data-test="add-to-cart-{product_key}"]'
            ).click()


    def assert_cart_badge_number(self, items_number: int):

        expect(self.page.locator(self.CART_BADGE)).to_have_text(items_number)

    def open_cart(self):
        self.page.locator(self.LINK_CART).click()
