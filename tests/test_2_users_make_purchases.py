from playwright.sync_api import Page, expect
from pages.login import Login_Page
from pages.listings import Listing_Page
from pages.cart import Cart_Page
from pages.checkout import Checkout_Page
import random

password = "secret_sauce"

PRODUCT_ITEMS_NAMES = ["sauce-labs-backpack", "sauce-labs-bike-light", "sauce-labs-bolt-t-shirt", "sauce-labs-fleece-jacket", "sauce-labs-onesie", "test.allthethings()-t-shirt-(red)"]

# def test_1_standard_user_make_purchase(page: Page, password, variables):
def test_1_standard_user_make_purchase(page: Page):
    """The cart contains the selected product, price, and quantity."""

    # login_page = Login_Page(page, variables)
    # listing_page = Listing_Page(page, variables)
    
    login_page = Login_Page(page)
    listing_page = Listing_Page(page)
    cart_page = Cart_Page(page)

    login_page.go_to_login()
    login_page.login("standard_user", password)

    chosen_items = random.sample(PRODUCT_ITEMS_NAMES, 3)

    for i in chosen_items:
        listing_page.add_product_to_cart(i)

    expect(page.locator(listing_page.CART_BADGE)).to_have_text("1")

    listing_page.open_cart()
    expect(page).to_have_url(cart.url)
    expect(page.locator(cart.TITLE)).to_have_text("Your Cart")
    expect(page.locator(cart.ITEMS)).to_have_count(1)

    item = cart.item_by_name(PRODUCT["name"])
    expect(item.locator(cart.PRODUCT_NAME)).to_have_text(
        PRODUCT["name"]
    )
    expect(item.locator(cart.PRODUCT_PRICE)).to_have_text(
        PRODUCT["price"]
    )
    expect(item.locator(cart.ITEM_QUANTITY)).to_have_text("1")


def test_2_unable_to_checkout(
    page: Page, password, variables, 
):
    """A customer can purchase a product and see order confirmation."""

    login_page = Login_Page(page, variables)
    listing_page = Listing_Page(page, variables)

    login_page.login(user, password)


    listing_page = logged_in_listing_page
    listing_page.add_product_to_cart(PRODUCT["name"])
    listing_page.open_cart()

    cart = Cart_Page(page)
    cart.start_checkout()

    checkout = Checkout_Page(page)
    checkout.fill_customer_details(**CHECKOUT_CUSTOMER)
    checkout.continue_to_overview()

    expect(page.locator(checkout.TITLE)).to_have_text("Checkout: Overview")
    expect(page.locator(checkout.ITEMS)).to_have_count(1)
    expect(page.locator(checkout.PRODUCT_NAME)).to_have_text(PRODUCT["name"])
    expect(page.locator(checkout.PRODUCT_PRICE)).to_have_text(PRODUCT["price"])

    checkout.finish_order()

    expect(page).to_have_url(checkout.complete_url)
    expect(page.locator(checkout.SUCCESS_MESSAGE)).to_have_text(ORDER_SUCCESS_MESSAGE)
