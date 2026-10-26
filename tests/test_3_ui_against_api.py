import pytest
import random
from playwright.sync_api import Page, expect
from utils.logger import log

@pytest.mark.xfail(reason="Fail bacause the API listings are in ascending order, but UI is not")
def test_1_assert_fragrance_listing_page(page: Page):
    """
        This test is specifically to assert UI against API, since the `saucedemo.com` is doesn't have any API response returned no matter what action
    """

    page.goto("https://dariuszmeissner.github.io/React-Store-theme/?utm_source=chatgpt.com")

    with page.expect_response("**/products/category/fragrances") as response_info:
    # with page.expect_response(lambda res: "**/products/category/fragrances" in res.url and res.status == 200) as response_info:
        log("Click on 'Discover' button")
        page.get_by_role("button", name="Discover").click()
        log(f"Expecting response '**/products/category/fragrances'...")

    response_code = response_info.value.status
    response_json = response_info.value.json()

    assert response_code == 200, f"Response status code is not 200, but {response_code} instead"
    products = response_json["products"]

    for i, product in enumerate(products):
        # because UI do not have good element identifier, will have t workaround to get Product Name, Proce
        actual_product = page.locator('div[class="product-teaser"]').nth(i)
        actual_product_text = actual_product.inner_text()

        expected_name = product["title"]
        expected_price = str(product["price"])

        log(f"Assert product in UI against API: {actual_product_text}")
        assert expected_name in actual_product_text, f"Expect to have product: {expected_name}"
        assert expected_price in actual_product_text, f"Expect to have product: {expected_price}"

    log("Assertion Complated!!!")
