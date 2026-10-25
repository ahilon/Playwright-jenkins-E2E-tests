from collections.abc import Iterator

import pytest
from playwright.sync_api import Browser, Page, expect

import playwright_jenkins_e2e.consts as Consts
from playwright_jenkins_e2e.jenkins_client import JenkinsClient
from playwright_jenkins_e2e.pages.login_page import LoginPage
from playwright_jenkins_e2e.settings import Settings


@pytest.fixture(scope="session")
def authenticated_storage_state(
    browser: Browser,
    tmp_path_factory: pytest.TempPathFactory,
    settings: Settings,
    base_url: str,
) -> str:
    """
    Fixture to create an authenticated storage state for the Jenkins application.
    args:
        browser: The Playwright Browser instance.
        tmp_path_factory: The pytest temporary path factory.
        settings: The Settings instance containing Jenkins credentials.
        base_url: The base URL of the Jenkins application.
    returns: The path to the storage state file.
    """
    state_path = tmp_path_factory.mktemp("playwright") / "auth.json"
    context = browser.new_context(base_url=base_url)

    try:
        page = context.new_page()
        LoginPage(page).login(
            username=settings.username,
            password=settings.password,
        )

        expect(page.get_by_role("link", name="New Item")).to_be_visible()

        context.storage_state(path=state_path)
    finally:
        context.close()

    return str(state_path)


@pytest.fixture(scope="session")
def browser_context_args(
    browser_context_args: dict, authenticated_storage_state: str
) -> dict:
    return {
        **browser_context_args,
        "storage_state": authenticated_storage_state,
        "locale": "en-US",
    }


@pytest.fixture
def jenkins_page(page: Page) -> Page:
    page.goto("/")
    return page


@pytest.fixture(scope="session")
def jenkins_client(settings: Settings) -> Iterator[JenkinsClient]:
    if settings.token is None:
        pytest.skip(f"{Consts.ENV_TOKEN} is not set")
    client = JenkinsClient(settings.url, settings.username, settings.token)
    yield client
    client.close()
