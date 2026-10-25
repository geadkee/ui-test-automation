import pytest
import random
from playwright.sync_api import Page, expect
from pages.listings import Listing_Page
from pages.login import Login_Page
from test_data.scenario_data import INVALID_LOGIN_CASES

password = "secret_sauce"

# def test_1_valid_users_able_to_login_and_access_page(page: Page, variables, password):
def test_1_valid_users_able_to_login_and_access_page(page: Page):
    """Valid credentials allow access to the product inventory."""

    # login_page = Login_Page(page, variables)
    # listing_page = Listing_Page(page, variables)
    login_page = Login_Page(page)
    listing_page = Listing_Page(page)

    login_page.go_to_login()
    login_page.login("standard_user", password)
    login_page.assert_access()

    listing_page.assert_listings()


# @pytest.mark.parametrize("case", INVALID_LOGIN_CASES, ids=[case["id"] for case in INVALID_LOGIN_CASES])
# def test_2_invalid_users_unable_to_login(page: Page, variables, password, case):
def test_2_invalid_users_unable_to_login(page: Page):
    """To make sure invalid users are unable to access the page, with proper error message"""


    login_page = Login_Page(page)
    listing_page = Listing_Page(page)

    login_page.go_to_login()
    login_page.login("locked_out_user", password)
    login_page.assert_access(has_access=False)


# to map access expectation with valid n invalid users
users_map = {
    "valid": {
        ""
    },
    "invalid": {
        ""
    }
}
