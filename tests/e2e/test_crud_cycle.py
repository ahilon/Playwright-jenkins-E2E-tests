from playwright.sync_api import Playwright, sync_playwright, expect

from playwright_jenkins_e2e.browser import launch_browser, start_tracing, stop_tracing
from playwright_jenkins_e2e.pages.login_page import LoginPage
from playwright_jenkins_e2e.pages.job_page import JobPage

SIMPLE_FREESTYLE = "simple_freestyle"
ECHO_COMMAND = "Build Created"


def run(playwright: Playwright) -> None:
    """
    Run the CRUD cycle test.
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
        job_page = JobPage(page)

        login_page.login()

        job_page.create_freestyle(SIMPLE_FREESTYLE)
        job_page.add_echo_build(ECHO_COMMAND)
        job_page.trigger_build(SIMPLE_FREESTYLE)

        expect(page.get_by_text("Finished: SUCCESS")).to_be_visible()
        expect(page.get_by_text(ECHO_COMMAND)).to_be_visible()
    finally:
        job_page.delete_project(SIMPLE_FREESTYLE)
        stop_tracing(context, "test_crud_cycle")
        context.close()
        browser.close()


with sync_playwright() as playwright:
    run(playwright)
