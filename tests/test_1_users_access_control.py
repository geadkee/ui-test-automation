import pytest
from playwright.sync.api import Page, expect 
import random
from pages.listings import Listing_Page
from pages.login import Login_Page

# to map access expectation with valid n invalid users
users_map = {
    "valid": {
        ""
    },
    "invalid": {
        ""
    }
}

def test_1_valid_users_able_to_login_and_access_page(page: Page, variables):
    """To ensure valid users are able to login successfully and view product listing page """
    login_page = Login_Page(page, variables)
    listing_page = Listing_Page(page, variables)
    


def test_2_invalid_users_unable_to_login(page: Page, variables):
    """To make sure invalid users are unable to access the page, with proper error message"""
