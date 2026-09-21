import re

from playwright.sync_api import Playwright, sync_playwright, expect

from playwright_jenkins_e2e.browser import launch_browser, start_tracing, stop_tracing


def run(playwright: Playwright) -> None:
    browser = launch_browser(playwright)
    context = browser.new_context(locale="en-US")
    start_tracing(context)
    page = context.new_page()

    try:
        page.goto("http://localhost:8080/login")
        page.get_by_label("Username").fill("testuser")
        page.get_by_label("Password").fill("testpass123")
        page.get_by_role("button", name="Sign in").click()

        expect(page).to_have_title(re.compile("Dashboard"))
        expect(page.get_by_role("link", name="New Item")).to_be_visible()
    finally:
        stop_tracing(context, "test_smoke")
        context.close()
        browser.close()


with sync_playwright() as playwright:
    run(playwright)
