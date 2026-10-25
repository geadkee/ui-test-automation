from playwright.sync_api import Page, expect


class Login_Page:
    INPUT_USERNAME = '[data-test="username"]'
    INPUT_PASSWORD = '[data-test="password"]'
    BUTTON_LOGIN = '[data-test="login-button"]'
    ERROR_MESSAGE = 'h3[data-test="error"]'
    ERROR_TEXT = 'Epic sadface: Sorry, this user has been locked out.'

    def __init__(self, page: Page):
        self.page = page
        # self.variables = variables
        # self.url = f"{self.variables['base_url']}/"
        self.url = "https://www.saucedemo.com/"

    def go_to_login(self):
        self.page.goto(self.url)

    def login(self, username: str, password: str):
        self.page.locator(self.INPUT_USERNAME).fill(username)
        self.page.locator(self.INPUT_PASSWORD).fill(password)
        self.page.locator(self.BUTTON_LOGIN).click()

    def assert_access(self, has_access: bool=True):
        if has_access:
            assert self.page.get_by_text("Products").is_visible()
            assert self.page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').is_visible()

        else:
            expect(self.page.locator(self.ERROR_MESSAGE)).to_have_text(self.ERROR_TEXT)
