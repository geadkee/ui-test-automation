import pytest
import random
from playwright.sync_api import Page
from pages.listings import Listing_Page
from pages.login import Login_Page
from test_data.scenario_data import INVALID_LOGIN_CASES


def test_1_valid_users_able_to_login_and_access_page(page: Page, variables, password):
    """Valid credentials allow access to the product inventory."""

    login_page = Login_Page(page, variables)
    listing_page = Listing_Page(page, variables)

    login_page.go_to_login()
    login_page.login("standard_user", password)
    login_page.assert_access()

    listing_page.assert_listings()


@pytest.mark.parametrize("case", INVALID_LOGIN_CASES, ids=[case["id"] for case in INVALID_LOGIN_CASES])
def test_2_invalid_users_unable_to_login(page: Page, variables, case):
    """To make sure invalid credentials are unable to login, with proper error message"""


    login_page = Login_Page(page, variables)

    login_page.go_to_login()
    # login_page.login("locked_out_user", password)
    login_page.login(case["username"], case["password"])
    login_page.assert_access(has_access=False, error=case["expected_error"])
