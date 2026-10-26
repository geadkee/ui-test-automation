from playwright.sync_api import Page, expect
from test_data.scenario_data import PRODUCTS
from utils.logger import log
from decimal import Decimal, ROUND_HALF_UP

class Checkout_Page:
    TITLE = '[data-test="title"]'
    # Checkout page one
    INPUT_FIRST_NAME = '[data-test="firstName"]'
    INPUT_LAST_NAME = '[data-test="lastName"]'
    INPUT_POSTAL_CODE = '[data-test="postalCode"]'
    BUTTON_CONTINUE = 'input[data-test="continue"]'

    # Checkout page two
    LABEL_QUANTITY = '[data-test="cart-quantity-label"]'
    LABEL_CART_DESC = '[data-test="cart-desc-label"]'
    ITEM = '[data-test="inventory-item"]'
    ITEM_QUANTITY = '[data-test="item-quantity"]'
    PRODUCT_NAME = '[data-test="inventory-item-name"]'
    PRODUCT_PRICE = '[data-test="inventory-item-price"]'

    PAYMENT_INFO_LABEL = '[data-test="payment-info-label"]'
    PAYMENT_INFO_VALUE = '[data-test="payment-info-value"]'
    SHIPPING_INFO_LABEL = '[data-test="shipping-info-label"]'
    SHIPPING_INFO_VALUE = '[data-test="shipping-info-value"]'
    TOTAL_INFO_LABEL = '[data-test="total-info-label"]'
    SUBTOTAL_LABEL = '[data-test="subtotal-label"]'
    TAX_LABEL = '[data-test="tax-label"]'
    TOTAL_LABEL = '[data-test="total-label"]'

    BUTTON_CANCEL = '[data-test="cancel"]'
    BUTTON_FINISH = '[data-test="finish"]'

    # Complete page
    COMPLETE_TITLE = '[data-test="complete-header"]'
    COMPLETE_TEXT = '[data-test="complete-text"]'
    COMPLETE_IMAGE = '[data-test="pony-express"]'
    BUTTON_BACK_HOME = '[data-test="back-to-products"]'
    BUTTON_GENERATE_PDF = '[data-test="generate-pdf-order"]'

    def __init__(self, page: Page, variables: dict):
        self.page = page
        self.variables = variables
        self.checkout_first_url = f"{self.variables['base_url'].rstrip('/')}/checkout-step-one.html"
        self.checkout_overview_url = f"{self.variables['base_url'].rstrip('/')}/checkout-step-two.html"
        self.checkout_complete_url = f"{self.variables['base_url'].rstrip('/')}/checkout-complete.html"

    def expected_checkout_calculation(self, chosen_items: dict):
        decimals = Decimal("0.01")
        tax_rate = Decimal("0.08")

        expected_subtotal = sum((Decimal(PRODUCTS[item]["price"]) for item in chosen_items))
        expected_tax = (expected_subtotal * tax_rate).quantize(decimals, rounding=ROUND_HALF_UP)
        expected_total = (expected_subtotal + expected_tax).quantize(decimals, rounding=ROUND_HALF_UP)

        return [expected_subtotal, expected_tax, expected_total]

    
    def get_amount(self, selector):
        text = self.page.locator(selector).inner_text()
        return Decimal(text.split("$")[1].strip()).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    def assert_and_fill_up_checkout_details(self, first_name: str, last_name: str, postcode: str):

        expect(self.page.locator(self.TITLE)).to_have_text("Checkout: Your Information")
        expect(self.page).to_have_url(self.checkout_first_url)
        expect(self.page.locator(self.INPUT_FIRST_NAME)).to_have_attribute("placeholder", "First Name")
        expect(self.page.locator(self.INPUT_LAST_NAME)).to_have_attribute("placeholder", "Last Name")
        expect(self.page.locator(self.INPUT_POSTAL_CODE)).to_have_attribute("placeholder", "Zip/Postal Code")

        expect(self.page.locator(self.BUTTON_CONTINUE)).to_have_value("Continue")
        expect(self.page.locator(self.BUTTON_CANCEL)).to_have_text("Cancel")

        self.page.locator(self.INPUT_FIRST_NAME).fill(first_name)
        self.page.locator(self.INPUT_LAST_NAME).fill(last_name)
        self.page.locator(self.INPUT_POSTAL_CODE).fill(postcode)

        self.page.locator(self.BUTTON_CONTINUE).click()

    def review_checkout_overview(self, chosen_items: dict):

        expect(self.page.locator(self.TITLE)).to_have_text("Checkout: Overview")
        expect(self.page).to_have_url(self.checkout_overview_url)

        expected_totals = self.expected_checkout_calculation(chosen_items)
        self.assert_checkout_items(chosen_items)
        self.assert_checkout_summary(expected_totals)

    def assert_checkout_items(self, chosen_items: dict):
        
        # ensure that the products selected are still there
        log("Assert that the products are still there in Checkout page")
        expect(self.page.locator(self.ITEM)).to_have_count(len(chosen_items))
        
        for index, item_code in enumerate(chosen_items):
            item = self.page.locator(self.ITEM).nth(index)
            actual_item = item.inner_text()
            expected_item = PRODUCTS[item_code]

            expect(self.page.locator(self.ITEM_QUANTITY).nth(index)).to_have_text("1")
            assert expected_item["name"] in actual_item, (f"Expected product name '{expected_item['name']}'")
            assert expected_item["description"] in actual_item, (f"Incorrect description for '{expected_item['name']}'")
            assert expected_item["price"] in actual_item, (f"Expected price '{expected_item['price']}' for '{expected_item['name']}'")

    def assert_checkout_summary(self, expected_totals: list):

        expected_subtotal = expected_totals[0]
        expected_tax = expected_totals[1]
        expected_total = expected_totals[2]

        actual_subtotal = self.get_amount(self.SUBTOTAL_LABEL)
        actual_tax = self.get_amount(self.TAX_LABEL)
        actual_total = self.get_amount(self.TOTAL_LABEL)

        expect(self.page.locator(self.PAYMENT_INFO_LABEL)).to_have_text("Payment Information:")
        expect(self.page.locator(self.PAYMENT_INFO_VALUE)).to_have_text("SauceCard #31337")
        expect(self.page.locator(self.SHIPPING_INFO_LABEL)).to_have_text("Shipping Information:")
        expect(self.page.locator(self.SHIPPING_INFO_VALUE)).to_have_text("Free Pony Express Delivery!")
        expect(self.page.locator(self.TOTAL_INFO_LABEL)).to_have_text("Price Total")
        expect(self.page.locator(self.SUBTOTAL_LABEL)).to_contain_text(f"Item total: $")
        expect(self.page.locator(self.TAX_LABEL)).to_contain_text(f"Tax: $")
        expect(self.page.locator(self.TOTAL_LABEL)).to_contain_text(f"Total: $")

        assert actual_subtotal == expected_subtotal, f"Item total: expected ${expected_subtotal}, got ${actual_subtotal}"
        assert actual_tax == expected_tax, f"Tax: expected ${expected_tax}, got ${actual_tax}"
        assert actual_total == expected_total, f"Total: expected ${expected_total}, got ${actual_total}"
        expect(self.page.locator(self.BUTTON_CANCEL)).to_be_enabled()
        expect(self.page.locator(self.BUTTON_FINISH)).to_be_enabled()

    def complete_order(self):
        self.page.locator(self.BUTTON_FINISH).click()

        self.page.get_by_text("Checkout: Complete!")

        expect(self.page).to_have_url(self.checkout_complete_url)
        expect(self.page.locator(self.COMPLETE_TITLE)).to_have_text("Thank you for your order!")
        expect(self.page.locator(self.COMPLETE_TEXT)).to_have_text("Your order has been dispatched, and will arrive just as fast as the pony can get there!")
        expect(self.page.locator(self.COMPLETE_IMAGE)).to_be_visible()
        expect(self.page.locator(self.COMPLETE_IMAGE)).to_have_attribute("src", "/assets/checkmark-VLWQafip.png")
        expect(self.page.locator(self.BUTTON_BACK_HOME)).to_have_text("Back Home")
        expect(self.page.locator(self.BUTTON_BACK_HOME)).to_be_enabled()
        expect(self.page.locator(self.BUTTON_GENERATE_PDF)).to_have_text("Generate PDF order")
        expect(self.page.locator(self.BUTTON_GENERATE_PDF)).to_be_enabled()

        log("Go back Home")
        self.page.locator(self.BUTTON_BACK_HOME).click
