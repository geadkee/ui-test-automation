from playwright.sync_api import Page, expect
from pages.login import Login_Page
from pages.listings import Listing_Page
from pages.cart import Cart_Page
from pages.checkout import Checkout_Page
from utils.logger import log
from test_data.scenario_data import PRODUCTS, CHECKOUT_DETAILS
import random


PRODUCT_ITEMS_NAMES = ["sauce-labs-backpack", "sauce-labs-bike-light", "sauce-labs-bolt-t-shirt", "sauce-labs-fleece-jacket", "sauce-labs-onesie", "test.allthethings()-t-shirt-(red)"]
FIRST_NAME = CHECKOUT_DETAILS["first_name"]
LAST_NAME = CHECKOUT_DETAILS["last_name"]
POSTCODE = CHECKOUT_DETAILS["postcode"]

def test_1_user_make_purchase(page: Page, variables, password):
    """User login -> add items to cart -> assert cart items -> go to checkout -> assert checkout -> complete checkout"""

    
    login_page = Login_Page(page, variables)
    listing_page = Listing_Page(page, variables)
    cart_page = Cart_Page(page, variables)
    checkout_page = Checkout_Page(page, variables)

    login_page.go_to_login()
    login_page.login("standard_user", password)
    random_num = random.randint(1, 6)
    chosen_items = random.sample(PRODUCT_ITEMS_NAMES, random_num)

    for name in chosen_items:
        log(f"Added '{name}' to cart")
        listing_page.add_product_to_cart_and_assert_button_change(name)

    # assert the Badge number at Cart
    log(f"assert that cart badge number is expected: {len(chosen_items)}")
    expect(page.locator(listing_page.CART_BADGE)).to_have_text(str(len(chosen_items)))

    log("User opening cart")
    listing_page.go_to_cart()
    cart_page.assert_cart_page()
    log("Check cart Items")
    cart_page.assert_cart_items(chosen_items)
    log("Proceed to Checkout")
    cart_page.go_to_checkout()

    log("Assert then fill up checkout details")
    checkout_page.assert_and_fill_up_checkout_details(FIRST_NAME, LAST_NAME, POSTCODE)
    log("Assert checkout overview")
    checkout_page.review_checkout_overview(chosen_items)
    log("Confirm checkout")
    checkout_page.complete_order()
