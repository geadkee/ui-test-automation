from playwright.sync_api import Page, expect
import random
from test_data.scenario_data import PRODUCTS
from utils.logger import log


class Listing_Page:
    TITLE = 'span[data-test="title"]'
    SORTING_VALUE = '[data-test="active-option"]'
    PRODUCT_CARDS = '[data-test="inventory-item"]'
    # BUTTON_ADD_TO_CART = 'button[data-test^="add-to-cart-"]'
    BUTTON_ADD_TO_CART = 'button[data-test="add-to-cart-{}"]'
    BUTTON_REMOVE_CART = 'button[data-test="remove-{}"]'
    CART_BADGE = '[data-test="shopping-cart-badge"]'
    LINK_CART = 'a[data-test="shopping-cart-link"]'

    PRODUCT_NAMES = '[data-test="inventory-item-name"]'

    PRODUCTS = {
        "sauce-labs-backpack": {
            "name": "Sauce Labs Backpack",
            "description": "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.",
            "price": "29.99",
            "image_src": "https://www.saucedemo.com/assets/sauce-backpack-1200x1500-CjRW-Djj.jpg",
        },
        "sauce-labs-bike-light": {
            "name": "Sauce Labs Bike Light",
            "description": "A red light isn't the desired state in testing but it sure helps when riding your bike at night. Water-resistant with 3 lighting modes, 1 AAA battery included.",
            "price": "9.99",
            "image_src": "https://www.saucedemo.com/assets/bike-light-1200x1500-DxcZRFOA.jpg",
        },
        "sauce-labs-bolt-t-shirt": {
            "name": "Sauce Labs Bolt T-Shirt",
            "description": "Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt.",
            "price": "15.99",
            "image_src": "https://www.saucedemo.com/assets/bolt-shirt-1200x1500-mR0ldpVS.jpg",
        },
        "sauce-labs-fleece-jacket": {
            "name": "Sauce Labs Fleece Jacket",
            "description": "It's not every day that you come across a midweight quarter-zip fleece jacket capable of handling everything from a relaxing day outdoors to a busy day at the office.",
            "price": "49.99",
            "image_src": "https://www.saucedemo.com/assets/sauce-pullover-1200x1500-BfbI-PSd.jpg",
        },
        "sauce-labs-onesie": {
            "name": "Sauce Labs Onesie",
            "description": "Rib snap infant onesie for the junior automation engineer in development. Reinforced 3-snap bottom closure, two-needle hemmed sleeved and bottom won't unravel.",
            "price": "7.99",
            "image_src": "https://www.saucedemo.com/assets/red-onesie-1200x1500-BrSuq0ic.jpg",
        },
        "test.allthethings()-t-shirt-(red)": {
            "name": "Test.allTheThings() T-Shirt (Red)",
            "description": "This classic Sauce Labs t-shirt is perfect to wear when cozying up to your keyboard to automate a few tests. Super-soft and comfy ringspun combed cotton.",
            "price": "15.99",
            "image_src": "https://www.saucedemo.com/assets/red-tatt-1200x1500-E-qp6aYf.jpg",
        },
    }


    def __init__(self, page: Page, variables: dict):
        self.page = page
        self.variables = variables
        self.url = f"{self.variables['base_url'].rstrip('/')}/inventory.html"

    def wait_until_loaded(self):
        expect(self.page).to_have_url(self.url)
        expect(self.page.locator(self.TITLE)).to_have_text("Products")

    def assert_listings(self, is_valid_user: bool=True):

        if is_valid_user:
            log(f"Assert url: {self.url}")
            expect(self.page).to_have_url(self.url)
            expect(self.page.locator(self.TITLE)).to_have_text("Products")
            expect(self.page.locator(self.PRODUCT_CARDS)).not_to_have_count(0)

            expect(self.page.locator(self.SORTING_VALUE)).to_have_text("Name (A to Z)")
            product_names = self.page.locator(self.PRODUCT_NAMES).all_text_contents()
            assert product_names == sorted(product_names), f"Product list is not sorted A to Z: {product_names}"

            for code, product in PRODUCTS.items():
                # 
                item = self.page.locator(self.PRODUCT_CARDS).filter(has_text=product["name"])
                actual_item = item.inner_text()

                log(f"Assert product's name, decription, price: '{actual_item}'")
                assert product["name"] in actual_item, (f"Expected product name '{product['name']}'")
                assert product["description"] in actual_item, (f"Incorrect description: '{product['description']}'")
                assert product["price"] in actual_item, (f"Expected price '{product['price']}' for '{product['name']}'")
                expect(self.page.locator(self.BUTTON_ADD_TO_CART.format(code))).to_be_enabled
                expect(self.page.locator(self.BUTTON_ADD_TO_CART.format(code))).to_have_text("Add to cart")

        else:
            print("Invalid user in listing page")


    def add_product_to_cart_and_assert_button_change(self, name: str):

        self.page.locator(self.BUTTON_ADD_TO_CART.format(name)).click()

        # after adding to cart, the button will change from "Add to Cart" to "Remove"
        expect(self.page.locator(self.BUTTON_ADD_TO_CART.format(name))).not_to_be_visible
        expect(self.page.locator(self.BUTTON_REMOVE_CART.format(name))).to_be_enabled
        expect(self.page.locator(self.BUTTON_REMOVE_CART.format(name))).to_have_text("Remove")

    def go_to_cart(self):
        self.page.locator(self.LINK_CART).click()
