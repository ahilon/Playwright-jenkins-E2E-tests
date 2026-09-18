from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(locale="en-US")
    page = context.new_page()
    try:
        page.goto("http://localhost:8080/")
        page.get_by_role("link", name="New Item").click()
        page.get_by_role("textbox", name="Enter an item name").fill("simple_freestyle")
        page.get_by_text("Freestyle projectClassic,").click()
        page.get_by_role("radio", name="Freestyle project Classic,").check()
        page.get_by_role("button", name="OK").click()
        page.get_by_role("button", name="Add build step").click()
        page.get_by_role("button", name="Execute shell").click()
        page.locator("section").filter(has_text="Build Steps Automate your").get_by_role("textbox").fill("echo \"build ok\"")
        page.get_by_role("button", name="Save").click()
        page.get_by_role("link", name="Build Now").click()
        page.locator("#jenkins-build-history").get_by_role("button").click()
        page.get_by_role("link", name="Console Output").click()
        expect(page.get_by_text("Finished: SUCCESS")).to_be_visible()
    finally:
        page.get_by_role("link", name="Jenkins", exact=True).click()
        page.get_by_role("link", name="simple_freestyle", exact=True).click()
        page.get_by_role("link", name="Delete Project", exact=True).click()
        page.get_by_role("button", name="Yes", exact=True).click()
        context.close()
        browser.close()


with sync_playwright() as playwright:
    run(playwright)
