from playwright.sync_api import Playwright, sync_playwright, expect

from playwright_jenkins_e2e.browser import launch_browser, start_tracing, stop_tracing
from playwright_jenkins_e2e.pages.login_page import LoginPage

WRONG_PASSWRORD = "wrongpassword"


def run(playwright: Playwright) -> None:
    """
    Run the negative smoke test.
    args:
        playwright: Playwright instance to use for the test.
    returns: None
    """
    browser = launch_browser(playwright)
    context = browser.new_context(locale="en-US")
    start_tracing(context)
    page = context.new_page()

    try:
        login_page = LoginPage(page)
        login_page.login(password = WRONG_PASSWRORD)
        expect(page.get_by_text("Invalid username or password")).to_be_visible()
    finally:
        stop_tracing(context, "test_smoke_negative")
        context.close()
        browser.close()


with sync_playwright() as playwright:
    run(playwright)
