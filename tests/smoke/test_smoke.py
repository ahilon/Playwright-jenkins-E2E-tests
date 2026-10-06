import re
import pytest

from playwright.sync_api import Page, expect

from playwright_jenkins_e2e.pages.login_page import LoginPage


@pytest.mark.smoke
def test_login_shows_dashboard(page: Page) -> None:
    """
    Run the smoke test.
    args: 
        page: Playwright page instance to use for the test.
    returns: None
    """

    LoginPage(page).login()

    expect(page).to_have_title(re.compile("Dashboard"))
    expect(page.get_by_role("link", name="New Item")).to_be_visible()

@pytest.mark.smoke
def test_login_shows_error_message_on_invalid_credentials(page: Page) -> None:
    """
    Run the negative smoke test.
    args: 
        page: Playwright page instance to use for the test.
    returns: None
    """

    LoginPage(page).login(password="wrongpassword")

    expect(page.get_by_text("Invalid username or password")).to_be_visible()
