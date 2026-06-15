from config import ADMIN_EMAIL, ADMIN_PASSWORD, BASE_URL
from playwright.sync_api import Page, expect


def test_validate_Admin_have_system_option(page: Page):
    """This test validates that after logging in as an admin, the 'System' option is available in the navigation menu."""

    page.goto(BASE_URL)

    page.locator("[data-test='input-email']").fill(ADMIN_EMAIL)
    page.locator("[data-test='input-password']").fill(ADMIN_PASSWORD)

    page.locator("[data-test='btn-login']").click()
    page.locator("[data-test='nav-system']").click()

    expect(page).to_have_url(
        'https://sv-students-recommend.onrender.com/pages/admin.html'
    )