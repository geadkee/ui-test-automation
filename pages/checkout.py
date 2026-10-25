from playwright.sync_api import Page


class Checkout_Page:
    TITLE = '[data-test="title"]'
    ITEMS = '[data-test="inventory-item"]'
    PRODUCT_NAME = '[data-test="inventory-item-name"]'
    PRODUCT_PRICE = '[data-test="inventory-item-price"]'
    SUCCESS_MESSAGE = '[data-test="complete-header"]'
    INPUT_FIRST_NAME = '[data-test="firstName"]'
    INPUT_LAST_NAME = '[data-test="lastName"]'
    INPUT_POSTAL_CODE = '[data-test="postalCode"]'
    BUTTON_CONTINUE = '[data-test="continue"]'
    BUTTON_FINISH = '[data-test="finish"]'

    def __init__(self, page: Page, variables):
        self.page = page
        self.variables = variables
        self.complete_url = f"{self.variables['base_url']}/checkout-complete.html"

    def fill_customer_details(self, first_name: str, last_name: str, postal_code: str):
        self.page.locator(self.INPUT_FIRST_NAME).fill(first_name)
        self.page.locator(self.INPUT_LAST_NAME).fill(last_name)
        self.page.locator(self.INPUT_POSTAL_CODE).fill(postal_code)

    def continue_to_overview(self):
        self.page.locator(self.BUTTON_CONTINUE).click()

    def finish_order(self):
        self.page.locator(self.BUTTON_FINISH).click()
