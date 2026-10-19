import pytest

from playwright.sync_api import Browser, expect, Page

import playwright_jenkins_e2e.consts as Consts
from playwright_jenkins_e2e.pages.login_page import LoginPage

@pytest.fixture(scope="session")
def authenticated_storage_state(
    browser: Browser,
    tmp_path_factory: pytest.TempPathFactory,
) -> str:
    """
    Fixture to create an authenticated storage state for the Jenkins application.
    args:
        browser: The Playwright Browser instance.
        tmp_path_factory: The pytest temporary path factory.
    returns: The path to the storage state file.
    """
    state_path = tmp_path_factory.mktemp("playwright") / "auth.json"
    context = browser.new_context()

    try:
        page = context.new_page()
        LoginPage(page).login()

        expect(page.get_by_role("link", name="New Item")).to_be_visible()

        context.storage_state(path=state_path)
    finally:
        context.close()

    return str(state_path)

@pytest.fixture(scope="session")
def browser_context_args(
    browser_context_args: dict,
    authenticated_storage_state: str
    ) -> dict:
    return {**browser_context_args,
            "storage_state": authenticated_storage_state,
             "locale": "en-US"
    }

@pytest.fixture
def jenkins_page(page: Page) -> Page:
    page.goto(Consts.LOCAL_HOST)
    return page
