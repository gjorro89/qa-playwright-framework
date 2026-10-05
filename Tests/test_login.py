import re
import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com/"

@pytest.mark.smoke
def test_standard_user_can_log_in(page: Page):
    page.goto(BASE_URL)

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url(re.compile(r".*/inventory\.html"))
    expect(page.locator('[data-test="title"]')).to_have_text("Products")