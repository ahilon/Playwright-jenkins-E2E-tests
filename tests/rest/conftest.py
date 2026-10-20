import pytest
import playwright_jenkins_e2e.consts as Consts
from playwright_jenkins_e2e.jenkins_client import JenkinsClient
from playwright_jenkins_e2e.settings import Settings

from collections.abc import Iterator


@pytest.fixture(scope="session")
def jenkins_client(settings: Settings) -> Iterator[JenkinsClient]:
    if settings.token is None:
        pytest.skip(f"{Consts.ENV_TOKEN} is not set")
    client = JenkinsClient(Consts.LOCAL_HOST, settings.username, settings.token)
    yield client
    client.close()