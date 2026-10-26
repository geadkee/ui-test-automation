from playwright.sync_api import Page, expect

class Login_Page:
    INPUT_USERNAME = '[data-test="username"]'
    INPUT_PASSWORD = '[data-test="password"]'
    BUTTON_LOGIN = '[data-test="login-button"]'
    ERROR_MESSAGE = 'h3[data-test="error"]'
    ERROR_TEXTBOX = ".error-message-container.error"

    def __init__(self, page: Page, variables: dict):
        self.page = page
        self.variables = variables
        self.url = f"{self.variables['base_url'].rstrip('/')}/"

    def go_to_login(self):
        self.page.goto(self.url)

    def login(self, username: str, password: str):
        self.page.locator(self.INPUT_USERNAME).fill(username)
        self.page.locator(self.INPUT_PASSWORD).fill(password)
        self.page.locator(self.BUTTON_LOGIN).click()

    def assert_access(self, error: dict=None, has_access: bool=True):
        if has_access:
            expect(self.page.get_by_text("Products")).to_be_visible()
            expect(self.page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')).to_be_visible()

        else:
            expect(self.page.locator(self.ERROR_MESSAGE)).to_have_text(error)
            expect(self.page.locator(self.BUTTON_LOGIN)).to_be_enabled()
            # expect(self.page.locator(self.ERROR_TEXTBOX)).to_have_css("color", "rgb(226, 35, 26)")

