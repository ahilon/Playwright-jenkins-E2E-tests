import re

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(locale="en-US")
    page = context.new_page()

    page.goto("http://localhost:8080/")
    expect(page).to_have_title(re.compile("Dashboard"))
    expect(page.get_by_role("link", name="New Item")).to_be_visible()

    page.get_by_role("link", name="Build History").click()
    expect(page).to_have_url(re.compile(r".*builds.*"))

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
