import pytest
from playwright_jenkins_e2e.settings import Settings

@pytest.fixture(scope="session")
def settings() -> Settings:
    return Settings.from_env()

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args: dict) -> dict:
    return {**browser_context_args, "locale": "en-US"}