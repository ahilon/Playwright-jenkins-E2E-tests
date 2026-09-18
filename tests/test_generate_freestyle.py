import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:8080/")
    page.get_by_role("link", name="Nowy projekt").click()
    page.get_by_role("textbox", name="Podaj nazwę projektu").click()
    page.get_by_role("textbox", name="Podaj nazwę projektu").fill("simple_freestyle")
    page.get_by_text("Ogólny projektClassic,").click()
    page.get_by_role("radio", name="Ogólny projekt Classic,").check()
    page.get_by_role("button", name="OK").click()
    page.get_by_role("button", name="Dodaj krok budowania").click()
    page.get_by_role("button", name="Uruchom powłokę").click()
    page.locator("section").filter(has_text="Kroki budowania Automate your").get_by_role("textbox").fill("echo \"build ok\"")
    page.get_by_role("button", name="Save").click()
    page.get_by_role("link", name="Uruchom").click()
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).click()
    page.get_by_role("link", name="Logi konsoli").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
